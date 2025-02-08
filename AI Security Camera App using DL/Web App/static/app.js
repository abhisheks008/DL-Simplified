document.addEventListener('DOMContentLoaded', () => {
    const detectionLog = document.getElementById('detection-log');
    
    function updateLog(detection) {
        const entry = document.createElement('div');
        entry.className = 'log-entry';
        entry.textContent = `${new Date().toLocaleTimeString()}: ${detection}`;
        detectionLog.prepend(entry);
        
        // Keep only last 50 entries
        while (detectionLog.children.length > 50) {
            detectionLog.removeChild(detectionLog.lastChild);
        }
    }
    
    // WebSocket connection would be implemented here
    // to receive real-time detection updates
});