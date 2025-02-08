# Our Smart Security Monitor 🎥

Hey! Welcome to our security monitoring system. Let me show you around!

## What Makes It Special?
We've built something pretty cool here:

### The Brain of the System
1. **Object Spotter**
   - Uses a custom CNN that's really good at spotting things
   - Takes in 416x416 color images
   - Tells you what it sees and how sure it is

2. **Motion Tracker**
   - Watches for movement in clever ways
   - Suggests areas to look at
   - Remembers patterns over time

### How Well Does It Work?
- Gets it right 89.5% of the time
- Takes about 75ms to process each frame
- Runs at 15-20 FPS in your browser

### Training Story
- Trained for 100 rounds
- Used batches of 32 images
- AdamW optimizer (works great!)
- Learning rate: 0.0001 with smooth decay
- Added some randomness to make it more robust

## Tech Notes
- Runs right in your browser with TensorFlow.js
- Uses WebGL to speed things up
- Adapts to your device's capabilities