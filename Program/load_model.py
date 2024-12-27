import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import randint

# Load and prepare training images
def load_real_samples(filename):
    # Load compressed arrays
    data = np.load(filename)
    # Unpack arrays
    X1, X2 = data['arr_0'], data['arr_1']
    # Scale from [0,255] to [-1,1]
    X1 = (X1 - 127.5) / 127.5
    X2 = (X2 - 127.5) / 127.5
    return [X1, X2]

# Plot source, generated and target images
def plot_images(src_img, gen_img, tar_img):
    # Stack images into a row for side-by-side display
    images = np.vstack((src_img, gen_img, tar_img))
    # Scale from [-1,1] to [0,1]
    images = (images + 1) / 2.0
    titles = ['Source', 'Generated', 'Expected']
    
    # Plot images row by row
    for i in range(len(images)):
        plt.subplot(1, 3, 1 + i)
        plt.axis('off')  # Turn off axis
        plt.imshow(images[i])  # Plot raw pixel data
        plt.title(titles[i])  # Show title
    
    plt.show()

# Load dataset
[X1, X2] = load_real_samples('maps_256.npz')
print('Loaded', X1.shape, X2.shape)

data = "D:/AI/folder_2/model_001096.h5"

# Load Pix2Pix model using TensorFlow
model = load_model(data)

# Select random example
ix = randint(0, len(X1), 1)
src_image, tar_image = X1[ix], X2[ix]

# Generate image from source image using the model
gen_image = model.predict(src_image)

# Plot all three images (source, generated, target)
plot_images(src_image, gen_image, tar_image)