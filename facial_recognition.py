import numpy as np
import statistics as stats
import math

# initialization for Question 2

class DataPoint(object):
    def __init__(self, cols):
        self.emotion = cols['emotion']
        self.pixels = cols['pixels']


# Normalize the images
def preprocessing(dataset):
    for i, image in enumerate(dataset):
        mean = stats.mean(image.pixels)
        stddev = np.std(image.pixels)
        adjusted_stddev = max(stddev, 1.0/math.sqrt(2304))
        print(image.pixels[0])
        for k, p in enumerate(image.pixels):
            image.pixels[k] = (p - mean) / adjusted_stddev
        print(image.pixels[0])


    return dataset

def parse_dataset(filename):
    data_file = open(filename, 'r')  # Open File "to read"
    dataset = []  # List to hold Datapoint objects
    # emotion_class = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

    for i, image in enumerate(data_file):
        if i == 0:
            continue # ignore headers
        emotion, pixelStr = image.strip().split(',')  # strip() removes '\n', and split(',') splits the line at tabs
        pixel_list = pixelStr.split()
        map_pixel = map(float, pixel_list)
        pixels = list(map_pixel)
        dataset.append(DataPoint({'emotion': emotion, 'pixels': pixels}))
        
    preprocessing(dataset)
    print("Number of samples by emotion: Angry - {0} , Disgust - {1} , Fear - {2} , Happy - {3} , Sad - {4} , Surprise - {5} , Neutral - {6}".format(len([i for i in dataset if i.emotion == '0']), len([i for i in dataset if i.emotion == '1']), len([i for i in dataset if i.emotion == '2']), len([i for i in dataset if i.emotion == '3']), len([i for i in dataset if i.emotion == '4']), len([i for i in dataset if i.emotion == '5']), len([i for i in dataset if i.emotion == '6'])))
    return dataset

parse_dataset('Q2_Train_Data.csv')
