import json
import tensorflow as tf
import cv2
import numpy as np



def predict(img,model,class_names):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    resize = tf.image.resize(img, (256,256))
    yhat = model.predict(np.expand_dims(resize/255,0))

    predicted_class = np.argmax(yhat)

    predicted_class_name = [k for k, v in class_names.items() if v == predicted_class][0]

    print(predicted_class_name)
    return predicted_class_name



    


    

    