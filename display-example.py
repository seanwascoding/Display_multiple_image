import numpy as np
import cv2

# read image
img = cv2.imread('./paper/00015-Yolov3tiny_output.bmp', cv2.IMREAD_COLOR)
print(type(img))
print(img.shape)

# display image
cv2.imshow('Demo test', img)

# distory image
cv2.waitKey(0)
cv2.destroyAllWindows()


# https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/