import cv2
from rest_framework import generics
from rest_framework.response import Response
from keras.models import load_model
from .serializers import ImageUploadSerializer
model_path = '/home/nandagopal/PycharmProjects/ImageClassifierApp/image_classifier/Model/trained_vgg16.h5'
dir_to_check = '/home/nandagopal/PycharmProjects/ImageClassifierApp/image_classifier/image_classifier'
from keras.applications.vgg16 import VGG16
from keras.layers import Dense
from keras.models import Sequential
from django.conf import settings
import numpy as np
import os
def prepare_model():
    Model = VGG16()
    model = Sequential()

    for layer in Model.layers[:-1]:
        model.add(layer)
    model.add(Dense(2, activation='softmax'))
    for layer in model.layers:
        layer.trainable = False


    model.load_weights(model_path)
    print(model.summary())
    return model

global Model
Model = prepare_model()

def prepare_image(image):
    img_path = os.path.join(dir_to_check, image)
    print(img_path)
    img_arr = cv2.resize(cv2.imread(img_path), dsize=(224, 224))
    print(img_arr.shape)
    return img_arr.reshape(1,224,224,3)

class Predict(generics.GenericAPIView):

    serializer_class = ImageUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print("Valid serializer")
        validated_data = serializer.validated_data
        saved_file_obj = serializer.save()
        saved_file_name = str(saved_file_obj).split('/')[-1]
        print("serializer.validated_data :", validated_data)
        print("saved_file_name" , saved_file_name)

        img_arr = prepare_image(saved_file_name)


        global Model
        prediction = Model.predict_proba(img_arr)
        D = {'Dog' : prediction[0][0],
             'Cat': prediction[0][1]}
        return Response(D)
