from flask import Flask
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import json 
import tensorflow as tf
from utils import predict,perform_action
#import tkinter as tk


app=Flask(__name__)

    

@app.route('/')
def home():
    model=tf.keras.models.load_model('model.h5')
    with open('class_names.json','r') as f:
        class_names=json.load(f)

    cap=cv2.VideoCapture(0)
    detector=HandDetector(maxHands=1)
    offset=20

    while True:
        ret,frame=cap.read()
        hands,frame=detector.findHands(frame)
        try:
            if hands:
                hand=hands[0]
                x,y,w,h=hand['bbox']

                imgCrop=frame[y-offset:y+h+offset,x-offset:x+w+offset]

                predicted_class_name=predict(imgCrop,model,class_names)

                perform_action(predicted_class_name)
        except:
            pass

        key=cv2.waitKey(1)

        if key==ord('q'):
            break


    return "Hello World"

if __name__=="__main__":
    print("Server is Starting")
    app.run(debug=True)