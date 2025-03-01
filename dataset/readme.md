Face Liveliness and Anti-Spoofing using Xception
This project implements face liveliness detection and anti-spoofing using a combination of Haar Cascade, Xception, and Shape Predictor. It aims to prevent spoofing attacks by detecting whether a face is real or fake.

📌 Features
✅ Face Detection using Haar Cascade
✅ Anti-Spoofing Model based on Xception
✅ Liveliness Detection using Shape Predictor
✅ Pre-trained Weights for improved performance
✅ Live Demo using Flask

🚀 Setup Instructions
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/YOUR-USERNAME/DL-Simplified.git
cd DL-Simplified
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Application
sh
Copy
Edit
python app.py
Now, open http://localhost:5000 in your browser to test the model.

🛠️ Working Mechanism
1️⃣ Face Detection: Uses Haar Cascade to detect the face in an image or video frame.
2️⃣ Anti-Spoofing Model: The Xception model classifies the detected face as real or spoof.
3️⃣ Liveliness Detection: Uses Shape Predictor (68 facial landmarks) to check facial movements (e.g., blink detection).

📂 Dataset
🔗 Download Dataset (https://www.kaggle.com/datasets/faber24/lcc-fasd)

🔍 Results & Performance
The Xception model accurately detects real vs. spoof faces
Shape Predictor enhances liveliness detection by tracking eye blinking and facial motion
Handles various spoofing methods: photo, video, and mask attacks
📜 License
This project is open-source under the MIT License.

google drive links for pre-traind model ,haar-cascade and shape-predictor
https://drive.google.com/drive/folders/1lhFBzo5wnBOqLLQlM2YxjJ2NV6fSgw9J?usp=drive_link