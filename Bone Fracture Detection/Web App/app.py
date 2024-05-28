from flask import Flask , render_template , request , redirect , url_for , send_from_directory
import os
import cv2
import json
from ultralytics import YOLO

model = YOLO('best_model.pt')
app = Flask(__name__)
app.config['UPLOAD_FILES'] = 'Uploads/'

@app.route("/" , methods = ['GET' , 'POST'])
def Home_page():
    if request.method == "GET":
        return render_template('home.html')
    else:
        file = request.files['Input Image']
        path = os.path.join(app.config['UPLOAD_FILES'] , file.filename)
    name = request.form['Name']
    with open('./static/Users.csv' , 'at') as docs:
        docs.write(name + '\n')
    file.save(path)
    return redirect(url_for('prediction' , class_name = predict(path) , filename = file.filename))    
        
    
def predict(path): 
    img = cv2.imread(path)
    results = model.predict(img)
    try:
        class_index = int(results[0].boxes.cls[0])
        class_name = results[0].names[class_index]
        x , y , w , h = list(map(int ,results[0].boxes.xywh[0]))

        if class_name == "humerus":
            class_name += " fracture"
            
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        font_thickness = 2

        cv2.rectangle(img, (x-w//2, y-h//2), ((x-w//2)+ w ,(y-h//2)+ h), (0, 0, 255),2)
        cv2.putText(img , class_name , (x-w//2, y-h//2-5) , font , font_scale ,(0, 0, 255), font_thickness)
        cv2.imwrite(path , img)
    except IndexError:
        return "No Fracture"
    return class_name

@app.route("/prediction/<class_name>/<filename>" , methods = ['GET'])
def prediction(class_name , filename):
    with open('./static/data.json' , 'rt') as file:
        data = json.load(file)
        desc = data[class_name.title()]['Description']
        symptoms = data[class_name.title()]['Symptoms']
    
    return render_template('result.html' , class_name = class_name , filename = filename , desc = desc , sympt = symptoms)

@app.route('/serve_image/<filename>' , methods = ['GET'])
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FILES'] , filename)

if __name__ == "__main__":
    app.run(debug = True)