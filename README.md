# Videocap
import cv2
vidcap = cv2.VideoCapture("/Users/lilyliu/Documents/ResearchProject/video/video_test.avi")
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("/Users/lilyliu/Documents/ResearchProject/data/images/frame%03d.png" % count, image)     # save frame as "img001.png" file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 30
