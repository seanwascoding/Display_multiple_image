import cv2
import os

image_folder = './paper/'

image_files = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".bmp")])

print(len(image_files))

cv2.namedWindow("Image Stream", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Stream", 416, 416)

for image_file in image_files:
    frame = cv2.imread(image_file)

    if frame is not None:
        cv2.imshow("Image Stream", frame)
        cv2.waitKey(100)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()