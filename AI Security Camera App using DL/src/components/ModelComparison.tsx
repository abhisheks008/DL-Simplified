import React from 'react';
import { BarChart, Activity, Zap } from 'lucide-react';

// Custom analytics based on security industry benchmarks
const SYSTEM_PERFORMANCE = {
  neuralEngine: {
    accuracy: 0.91,
    inferenceTime: 80,
    mAP: 0.89
  },
  motionProcessor: {
    accuracy: 0.88,
    inferenceTime: 95,
    mAP: 0.86
  },
  objectTracker: {
    accuracy: 0.87,
    inferenceTime: 110,
    mAP: 0.85
  }
};

// Environment analysis metrics
const ENVIRONMENT_METRICS = {
  distribution: {
    individual: 148500,
    dangerous: 49500,
    carried: 82500,
    misc: 49500
  },
  conditions: {
    controlled: 165000,
    variable: 165000
  }
};

export function SystemMetrics() {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mt-8">
      <div className="flex items-center gap-2 mb-4">
        <Activity className="w-6 h-6 text-indigo-600" />
        <h2 className="text-xl font-bold">System Performance Analysis</h2>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {Object.entries(SYSTEM_PERFORMANCE).map(([engine, metrics]) => (
          <div key={engine} className="border rounded-xl p-4">
            <h3 className="text-lg font-semibold mb-2 capitalize">{engine.replace(/([A-Z])/g, ' $1').trim()}</h3>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span className="text-slate-600">Recognition Rate:</span>
                <span className="font-medium">{(metrics.accuracy * 100).toFixed(1)}%</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-600">Processing Time:</span>
                <span className="font-medium">{metrics.inferenceTime}ms</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-600">Precision Score:</span>
                <span className="font-medium">{metrics.mAP.toFixed(2)}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-8">
        <div className="flex items-center gap-2 mb-4">
          <BarChart className="w-6 h-6 text-indigo-600" />
          <h2 className="text-xl font-bold">Environmental Analysis</h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="border rounded-xl p-4">
            <h3 className="text-lg font-semibold mb-2">Object Classification</h3>
            <div className="space-y-2">
              {Object.entries(ENVIRONMENT_METRICS.distribution).map(([category, count]) => (
                <div key={category} className="flex justify-between">
                  <span className="capitalize text-slate-600">{category}:</span>
                  <span className="font-medium">{count.toLocaleString()} instances</span>
                </div>
              ))}
            </div>
          </div>

          <div className="border rounded-xl p-4">
            <h3 className="text-lg font-semibold mb-2">Environmental Conditions</h3>
            <div className="space-y-2">
              {Object.entries(ENVIRONMENT_METRICS.conditions).map(([condition, count]) => (
                <div key={condition} className="flex justify-between">
                  <span className="capitalize text-slate-600">{condition}:</span>
                  <span className="font-medium">{count.toLocaleString()} samples</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      <div className="mt-6 p-4 bg-indigo-50 rounded-xl">
        <div className="flex items-center gap-2 mb-2">
          <Zap className="w-5 h-5 text-indigo-600" />
          <h3 className="font-semibold">Performance Insights</h3>
        </div>
        <ul className="list-disc list-inside space-y-1 text-sm text-slate-700">
          <li>Neural engine achieves optimal balance of speed and accuracy</li>
          <li>Individual detection shows highest reliability due to extensive training data</li>
          <li>System performs consistently across varied environments</li>
          <li>Controlled conditions yield 12% higher accuracy rates</li>
        </ul>
      </div>
    </div>
  );
}