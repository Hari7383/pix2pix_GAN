import os
import cv2
import glob

input_dir = 'D:/AI/MY_data/facades/train'
output_dir = 'D:/AI/MY_data/facades/segmentaion'  

os.makedirs(os.path.join(output_dir, 'input_images'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'label_images'), exist_ok=True)

image_files = glob.glob(f'{input_dir}/*.jpg')

for filepath in image_files:
    
    image = cv2.imread(filepath)

    height, width, channels = image.shape
    print(f"Processing {os.path.basename(filepath)} - Dimensions: Height={height}, Width={width}")

    input_image = image[:, :width//2]   
    label_image = image[:, width//2:]   

    # Save the segmented images
    filename = os.path.basename(filepath)
    cv2.imwrite(os.path.join(output_dir, 'input_images', filename), input_image)
    cv2.imwrite(os.path.join(output_dir, 'label_images', filename), label_image)

print("Processing complete!")