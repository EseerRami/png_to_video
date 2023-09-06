import cv2
import os

# Path to the folder containing PNG images
image_folder = 'images'
# Get all files from the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

# Sort the images by their numerical value
images.sort(key=lambda x: int(x.split('.')[0]))

# Create a VideoCapture object
frame = cv2.imread(os.path.join(image_folder, images[0]))

# Setting the frame width, height width
# the width, height of an image (assuming the first image's size as standard)
height, width, layers = frame.shape

# Initialize the video writer with 30 fps
video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# Number of times to write the same frame to make it appear for 1 second
frame_repeat = 2  # 30 frames for 1 second at 30 fps

# Appending the images to the video one by one
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    
    # Resize the frame to match the video dimensions
    resized_frame = cv2.resize(frame, (width, height))
    
    for _ in range(frame_repeat):
        video.write(resized_frame)

# Deallocating memories taken for window creation
cv2.destroyAllWindows()
video.release()  # releasing the video generated