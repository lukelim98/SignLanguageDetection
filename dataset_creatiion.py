import mediapipe
import cv2
import os
import matplotlib.pyplot as plt

DATA_DIR = './data'

for dir_ in os.listdir(DATA_DIR):
    for image_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:
        image = cv2.imread(os.path.join(DATA_DIR, dir_, image_path))
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        plt.imshow(image_rgb)


