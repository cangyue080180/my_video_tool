import cv2
import os

# 需要读取的视频文件路径
file_name = 'test.mp4'
pic_save_path = 'pics'
pic_ends = '.jpg'
use_max_index = False
max_read_index = 20

if not os.path.exists(pic_save_path):
    os.makedirs(pic_save_path)

capture = cv2.VideoCapture(file_name)
index = 1
ret, frame = capture.read()
while ret:
    resize_frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(pic_save_path, str(index)+pic_ends), resize_frame)
    index += 1
    ret, frame = capture.read()

    if use_max_index and index > max_read_index:
        break

capture.release()
