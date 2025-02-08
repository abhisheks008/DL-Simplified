import React from 'react';
import { Shield } from 'lucide-react';
import { CameraMonitor } from './components/WebcamDetection';
import { SystemMetrics } from './components/ModelComparison';

function App() {
  return (
    <div className="min-h-screen bg-slate-100">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex items-center gap-2">
            <Shield className="w-8 h-8 text-indigo-600" />
            <h1 className="text-2xl font-bold text-slate-900">Intelligent Security Monitor</h1>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="bg-white rounded-xl shadow-lg p-6">
          <div className="max-w-3xl mx-auto">
            <div className="text-center mb-8">
              <h2 className="text-3xl font-bold text-slate-900">Advanced Threat Detection System</h2>
              <p className="mt-2 text-slate-600">
                Real-time security monitoring powered by computer vision and deep learning
              </p>
            </div>
            
            <CameraMonitor />
            <SystemMetrics />
            
            <div className="mt-8 p-4 bg-indigo-50 rounded-xl">
              <h3 className="text-lg font-semibold text-indigo-900 mb-2">System Capabilities:</h3>
              <ul className="list-disc list-inside text-indigo-800 space-y-2">
                <li>Real-time threat detection with advanced algorithms</li>
                <li>Multi-object recognition and classification</li>
                <li>Continuous motion analysis</li>
                <li>Performance monitoring and analytics</li>
              </ul>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;