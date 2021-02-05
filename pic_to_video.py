import os
import cv2

pics_file_path = 'pics'
pic_ends = '.jpg'
end_index = 8917
frame_speed_one_second = 30
pic_width = 1280
pic_height = 720
start_index = 1

fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
video_writer = cv2.VideoWriter('output.mp4', fourcc, frame_speed_one_second, (pic_width, pic_height))
while start_index <= end_index:
    if not os.path.exists(os.path.join(pics_file_path, str(start_index)+pic_ends)):
        continue
    pic = cv2.imread(os.path.join(pics_file_path, str(start_index)+pic_ends))
    # cv2.imshow('pic', pic)
    # cv2.waitKey(40)
    video_writer.write(pic)

    start_index += 1

# cv2.destroyAllWindows()
video_writer.release()