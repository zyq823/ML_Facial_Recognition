import tensorflow as tf

# initialization for Question 2

class DataPoint(object):
    def __init__(self, cols):
        self.emotion = cols['emotion']
        self.pixels = cols['pixels']

    def __str__(self):
        return "emotion: {}".format(self.emotion)

def parse_dataset(filename):
    data_file = open(filename, 'r')  # Open File "to read"
    dataset = []  # List to hold Datapoint objects
    # emotion_class = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

    for image in data_file:
        emotion, pixels = image.strip().split(',')  # strip() removes '\n', and split(',') splits the line at tabs
        # print(emotion)
        dataset.append(DataPoint({'emotion': emotion, 'pixels': pixels}))
        
    print(len(dataset))
    print("Number of samples by emotion: Angry - {0} , Disgust - {1} , Fear - {2} , Happy - {3} , Sad - {4} , Surprise - {5} , Neutral - {6}".format(len([i for i in dataset if i.emotion == '0']), len([i for i in dataset if i.emotion == '1']), len([i for i in dataset if i.emotion == '2']), len([i for i in dataset if i.emotion == '3']), len([i for i in dataset if i.emotion == '4']), len([i for i in dataset if i.emotion == '5']), len([i for i in dataset if i.emotion == '6'])))
    return dataset

parse_dataset('Q2_Train_Data.csv')