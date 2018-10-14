import cv2
vidcap = cv2.VideoCapture("/Users/lilyliu/Documents/ResearchProject/video/video_test.avi")
success,image = vidcap.read()
count = 0
while success:
  if count % 30 == 0:
    cv2.imwrite("/Users/lilyliu/Documents/ResearchProject/data/images/img%03d.png" % count, image)          
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1  # count = count + 1
