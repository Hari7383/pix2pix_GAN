import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import os

# Function to load the saved generator model
def load_generator_model(model_path):
    return load_model(model_path)

# Function to load and preprocess a new image
def load_and_preprocess_image(image_path, target_size=(256, 256)):
    # Load image
    img = load_img(image_path, target_size=target_size)
    # Convert image to numpy array
    img_array = img_to_array(img)
    # Rescale from [0, 255] to [-1, 1]
    img_array = (img_array / 127.5) - 1
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to generate an output image from the generator model
def generate_image(generator_model, input_image):
    generated_image = generator_model.predict(input_image)
    return generated_image[0]  # Remove batch dimension

# Function to plot and save the original and generated image
def plot_images(original_image, generated_image):
    # Rescale from [-1, 1] to [0, 1] for display
    original_image = (original_image + 1) / 2.0
    generated_image = (generated_image + 1) / 2.0

    # Plot original and generated images
    plt.figure(figsize=(8, 4))
    
    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(generated_image)
    plt.title("Generated Image")
    plt.axis('off')
    
    # Save the plot to a file
    plt.savefig('generated_image.png')
    plt.show()

# Example usage after training:
if __name__ == '__main__':
    # Load your trained generator model
    generator_model = load_generator_model('D:/AI/facades_1/model_004000.h5')
    
    # Upload a new image for testing
    image_path = 'D:/AI/MY_data/maps/segmentaion/input_images/970.jpg'  
    if not os.path.exists(image_path):
        print(f"Image {image_path} not found!")
        exit()
    
    # Preprocess the new image
    input_image = load_and_preprocess_image(image_path)
    
    # Generate a transformed image using the trained generator
    generated_image = generate_image(generator_model, input_image)
    
    # Plot and save the original and generated images
    original_image = img_to_array(load_img(image_path, target_size=(256, 256)))  # Load original image to display
    original_image = original_image / 255.0 
    plot_images(original_image, generated_image)

