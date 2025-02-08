import React, { useRef, useEffect, useState, useCallback } from 'react';
import * as tf from '@tensorflow/tfjs';
import * as cocossd from '@tensorflow-models/coco-ssd';
import { AlertTriangle, Shield, Siren } from 'lucide-react';
import { Detection } from '../types/detection';
import { loadSecurityModel } from '../utils/modelLoader';

// Security settings
const MIN_CONFIDENCE = 0.28;
const VIDEO_FPS = 24;
const FRAME_TIME = 1000 / VIDEO_FPS;

// Objects to track
const TRACKED_ITEMS = {
  PERSON: 'person',
  KNIFE: 'knife',
  SCISSORS: 'scissors',
  BAT: 'baseball_bat',
  BOTTLE: 'bottle',
  PHONE: 'phone',
  BACKPACK: 'backpack',
  BAG: 'handbag',
  CASE: 'suitcase'
};

const HIGH_RISK_ITEMS = [TRACKED_ITEMS.KNIFE, TRACKED_ITEMS.SCISSORS, TRACKED_ITEMS.BAT];

// Convert standard labels to security terms
function convertToSecurityTerms(label) {
  const securityTerms = {
    [TRACKED_ITEMS.PERSON]: 'person',
    [TRACKED_ITEMS.KNIFE]: 'edged-weapon',
    [TRACKED_ITEMS.SCISSORS]: 'sharp-tool',
    [TRACKED_ITEMS.BAT]: 'blunt-weapon',
    [TRACKED_ITEMS.BOTTLE]: 'container',
    [TRACKED_ITEMS.PHONE]: 'device',
    [TRACKED_ITEMS.BACKPACK]: 'bag',
    [TRACKED_ITEMS.BAG]: 'carried-item',
    [TRACKED_ITEMS.CASE]: 'luggage'
  };
  return securityTerms[label.toLowerCase()] || label;
}

export function CameraMonitor() {
  const video = useRef(null);
  const overlay = useRef(null);
  const [detector, setDetector] = useState(null);
  const [isStarting, setIsStarting] = useState(true);
  const [error, setError] = useState(null);
  const [detectedObjects, setDetectedObjects] = useState([]);
  const frameLoop = useRef();
  const lastFrame = useRef(0);

  const processFrame = useCallback(async (time) => {
    if (!detector || !video.current || !overlay.current) {
      frameLoop.current = requestAnimationFrame(processFrame);
      return;
    }

    const elapsed = time - lastFrame.current;
    if (elapsed < FRAME_TIME) {
      frameLoop.current = requestAnimationFrame(processFrame);
      return;
    }
    lastFrame.current = time;

    const ctx = overlay.current.getContext('2d');
    if (!ctx) return;

    try {
      if (!isVideoReady(video.current)) {
        frameLoop.current = requestAnimationFrame(processFrame);
        return;
      }

      updateCanvasSize(overlay.current, video.current);
      ctx.clearRect(0, 0, overlay.current.width, overlay.current.height);
      ctx.drawImage(video.current, 0, 0);

      const objects = await detector.detect(video.current);
      if (!objects?.length) {
        frameLoop.current = requestAnimationFrame(processFrame);
        return;
      }

      const threats = objects
        .filter(item => item.score > MIN_CONFIDENCE)
        .map(item => ({
          area: item.bbox,
          type: convertToSecurityTerms(item.class),
          confidence: item.score,
          time: Date.now()
        }));

      setDetectedObjects(threats);
      drawDetections(ctx, threats);
    } catch (err) {
      console.warn('Frame processing error:', err);
      if (err.message !== 'No objects detected') {
        setError('Detection error - retrying...');
      }
    }

    frameLoop.current = requestAnimationFrame(processFrame);
  }, [detector]);

  function isVideoReady(video) {
    return video.readyState === video.HAVE_ENOUGH_DATA && 
           video.videoWidth && 
           video.videoHeight;
  }

  function updateCanvasSize(canvas, video) {
    if (canvas.width !== video.videoWidth || 
        canvas.height !== video.videoHeight) {
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
    }
  }

  function drawDetections(ctx, items) {
    items.forEach(item => {
      try {
        const [x, y, w, h] = item.area;
        const dangerous = HIGH_RISK_ITEMS.includes(item.type);
        
        // Draw box
        ctx.lineWidth = 3;
        ctx.strokeStyle = dangerous ? '#b91c1c' : '#c2410c';
        ctx.strokeRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h));
        
        // Draw label
        const text = dangerous 
          ? `WARNING: ${item.type} (${Math.round(item.confidence * 100)}%)`
          : `ALERT: ${item.type} (${Math.round(item.confidence * 100)}%)`;
        
        ctx.font = '14px monospace';
        const measure = ctx.measureText(text);
        const labelY = y > 25 ? y - 25 : y + h;
        
        ctx.fillStyle = dangerous ? '#b91c1c99' : '#c2410c99';
        ctx.fillRect(x, labelY, measure.width + 10, 25);
        
        ctx.fillStyle = '#fff';
        ctx.fillText(text, x + 5, labelY + 17);
      } catch (err) {
        console.warn('Drawing error:', err);
      }
    });
  }

  useEffect(() => {
    async function initCamera() {
      try {
        await tf.setBackend('webgl');
        await tf.ready();
        const model = await loadSecurityModel();
        setDetector(model);
        setIsStarting(false);
        setError(null);
      } catch (err) {
        console.error('Setup error:', err);
        setError('Failed to start security system');
        setIsStarting(false);
      }
    }

    initCamera();
    return () => {
      if (frameLoop.current) {
        cancelAnimationFrame(frameLoop.current);
      }
    };
  }, []);

  useEffect(() => {
    if (!detector) return;

    async function startCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: { 
            facingMode: 'environment',
            width: { ideal: 1920 },
            height: { ideal: 1080 },
            frameRate: { ideal: VIDEO_FPS }
          },
          audio: false
        });
        
        if (video.current) {
          video.current.srcObject = stream;
          video.current.onloadeddata = () => {
            requestAnimationFrame(processFrame);
          };
        }
      } catch (err) {
        console.error('Camera error:', err);
        setError('Camera access failed - check permissions');
      }
    }

    startCamera();

    return () => {
      const stream = video.current?.srcObject;
      stream?.getTracks().forEach(track => track.stop());
    };
  }, [detector, processFrame]);

  return (
    <div className="relative w-full h-screen flex flex-col p-4">
      <div className="relative flex-1 min-h-0">
        <video
          ref={video}
          autoPlay
          playsInline
          muted
          className="w-full h-full object-contain rounded-lg shadow-lg"
        />
        <canvas
          ref={overlay}
          className="absolute top-0 left-0 w-full h-full"
        />
      </div>

      <div className="mt-4">
        {isStarting ? (
          <div className="text-center p-4 bg-blue-100 rounded-lg">
            <p className="text-blue-800">Starting security system...</p>
          </div>
        ) : error ? (
          <div className="text-center p-4 bg-red-100 rounded-lg">
            <div className="flex items-center justify-center gap-2 text-red-800">
              <AlertTriangle className="w-5 h-5" />
              <p>{error}</p>
            </div>
          </div>
        ) : (
          <div className={`p-4 rounded-lg ${
            detectedObjects.length ? 'bg-red-100 animate-pulse' : 'bg-green-100'
          }`}>
            <div className="flex flex-col gap-2">
              {detectedObjects.length ? (
                <>
                  <div className="flex items-center gap-2">
                    <Siren className="w-6 h-6 text-red-500 animate-pulse" />
                    <span className="text-red-700 font-bold text-lg">
                      Security Alert: Objects Detected
                    </span>
                  </div>
                  <ul className="list-disc list-inside space-y-1">
                    {detectedObjects.map((obj, idx) => (
                      <li 
                        key={`${obj.type}-${idx}`}
                        className={
                          HIGH_RISK_ITEMS.includes(obj.type)
                            ? 'text-red-600 font-bold'
                            : 'text-orange-600'
                        }
                      >
                        {obj.type} detected ({Math.round(obj.confidence * 100)}% confidence)
                      </li>
                    ))}
                  </ul>
                </>
              ) : (
                <div className="flex items-center gap-2">
                  <Shield className="w-5 h-5 text-green-500" />
                  <span className="text-green-700 font-medium">
                    Area secure - No threats detected
                  </span>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}