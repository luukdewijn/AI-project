import xml.etree.ElementTree as ET
import pandas as pd
from PIL import Image
import numpy as np
import os


def convert_image(directory, image_file, width, height):
    # Open the image file
    img = Image.open(os.path.join(directory, image_file))
    # Resize the image
    img = img.resize((width, height))

    # Convert the image to grayscale
    img = img.convert('L')

    # Convert the image data to a numpy array
    image = np.array(img)

    # Flatten the array if your model expects a 1D input
    image = image.flatten()

    return image


def get_input_data(directory):
    images = [image for image in os.listdir(directory) if image.endswith('.png')]
    input_data = np.empty((len(images), (1024*1024)))
    for i in range(len(images)):
        image = convert_image(directory, images[i], 1024, 1024)
        input_data[i, :] = image
    return input_data
    

def get_output_data(file):
    # Parse the XML file and get the root
    tree = ET.parse(file)
    root = tree.getroot()

    # Create a list to store the data
    data = []

    # Iterate over each 'roll' element in the root
    for roll in root.findall('roll'):
        # Extract the 'image', 'die-one', and 'die-two' values
        image = roll.find('image').text
        die_one = roll.find('die-one').text
        die_two = roll.find('die-two').text

        # Store these values in a dictionary
        data.append({'image': image, 'die_one': die_one, 'die_two': die_two})

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

