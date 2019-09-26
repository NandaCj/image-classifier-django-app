# dataset download path = 'https://www.microsoft.com/en-us/download/details.aspx?id=54765&WT.mc_id=rss_alldownloads_devresources'
import os
from os.path import dirname, join
from os import listdir
import numpy as np
import pandas as pd
import tensorflow as tf
import keras
import pydot
from matplotlib import pyplot as plt
from keras import Input, Model, layers, Sequential
from keras.layers import Dense, Dropout

cur_dir = dirname(__file__)
dataset_dir = join(cur_dir, '../dataset_cats_dogs/PetImages')
cats_dir = join(dataset_dir, 'Cat')
dogs_dir = join(dataset_dir, 'Dog')

for file in listdir(cats_dir):
    print(file)

