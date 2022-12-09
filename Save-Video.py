import cv2 as cv

# The First step towards reading a video file is creating an object of video capture class.
# Its argument can be either the device index or the name of the video file to be read.
# We will first read from the camera of the device if you have only 1 camera connected to the system, we pass 0
vid = cv.VideoCapture("C:/Users/prath/OneDrive/Documents/Python/Creating_A_Video/PRO-C105-Teacher-Boilerplate/AnthonyShkraba.mp4")

# Use isOpened function. It returns true if Video Capture function has worked successfully.
# If the result is false, we will print, "Unable to Read the Feed"
if(vid.isOpened() == False):
    print("Unable to read the Feed") 

# Properties of any video can be read using GET method of video capture class.
# The values of the properties returned will be in float
height  = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))
print(width)

fps = int(vid.get(cv.CAP_PROP_FPS))
print(fps)

# Video Writer helps us to save the video in the local system/
# 
out = cv.VideoWriter('Boxing.avi', cv.VideoWriter_fourcc(*'MP4V'), 30, (width, height))

while(True):
    rep,frame = vid.read()
    
    out.write(frame)

    if cv.waitKey(25) == 32:
        break

vid.release()
out.release()
cv.destroyAllWindows()