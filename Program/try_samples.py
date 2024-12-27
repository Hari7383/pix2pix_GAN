'''from PIL import Image 
  
# get image 
filepath = "D:/AI/MY_data/maps/segmentaion/input_images/12.jpg"
image = Image.open(filepath) 



# Resize the image to (256, 256)
resized_image = image.resize((256, 256))

# Save or display the resized image
resized_image.save("resized_image.jpg")
resized_image.show()

path = 'D:/AI/resized_image.jpg'
img= Image.open(path) 
# get width and height 
width = img.width 
height = img.height 
  
# display width and height 
print("The height of the image is: ", height) 
print("The width of the image is: ", width) '''

'''for i in range(100):
    if i+1 == 100:
        print("if's i = ",i)
    print("for's i = ",i)'''