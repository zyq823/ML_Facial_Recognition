import numpy as np
import math
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
# from keras.utils import to_categorical

# from keras.models import Sequential
# from keras.layers import Dense, Dropout


# initialization for Question 2

def parse_dataset(filename):
    data_file = open(filename, 'r')  # Open File "to read"
    
    images = []
    labels = []

    for i, image in enumerate(data_file):
        if i == 0:
            continue # ignore headers
        emotion, pixelStr = image.strip().split(',')  # strip() removes '\n', and split(',') splits the line at tabs
        pixel_list = pixelStr.split()
        map_pixel = map(float, pixel_list)
        pixels = list(map_pixel)
        # image_pixels = [pixels[i:i+48] for i in range(0, len(pixels), 48)]
        
        labels.append(int(emotion)) # integer strings
        images.append(pixels) # integer list
    image1D = np.array(images)
    label1D = np.array(labels)
    image3D = image1D.reshape(len(labels), 48, 48)
        
    # print("Number of samples by emotion: Angry - {0} , Disgust - {1} , Fear - {2} , Happy - {3} , Sad - {4} , Surprise - {5} , Neutral - {6}".format(len([i for i in dataset if i.emotion == '0']), len([i for i in dataset if i.emotion == '1']), len([i for i in dataset if i.emotion == '2']), len([i for i in dataset if i.emotion == '3']), len([i for i in dataset if i.emotion == '4']), len([i for i in dataset if i.emotion == '5']), len([i for i in dataset if i.emotion == '6'])))
    return image3D, label1D

train_images, train_labels = parse_dataset('Q2_Train_Data.csv')
# valid_images, valid_labels = parse_dataset('Q2_Validation_Data.csv')
# test_set = parse_dataset('Q2_Test_Data.csv')


# print("Visualizing 28th image for Anger. ")
# print("Visualizing 300th image for Disgust. ")
# print("Visualizing 3rd image for Fear. ")
# print("Visualizing 8th image for Happy. ")
# print("Visualizing 20th image for Sad. ")
# print("Visualizing 16th image for Surprise. ")
# print("Visualizing 14th image for Neutral. ")
# _ = plt.imshow(train_images[13])
# print(type(train_images))
# print(train_labels)
# print(train_images[2,:,:])
# plt.show()


# Normalize the images
def preprocessing(dataset):
    for image in dataset:
        mean = np.mean(image)
        stddev = np.std(image)
        adjusted_stddev = max(stddev, 1.0/math.sqrt(2304))
        for p, row in enumerate(image):
            for q, col in enumerate(row):
                 image[p][q] = (col - mean) / adjusted_stddev

preprocessing(train_images)

# preprocessing(valid_images)
# preprocessing(test_images)

# model = Sequential([
#     Dense(784, activation='relu', input_shape=(28*28,), name="first_hidden_layer"),
#     Dense(784//2, activation='relu', name="second_hidden_layer"), Dropout(0.25),
#     Dense(10, activation='softmax'),
# ])

