import cv2
import os
import numpy as np

# 在图形的指定区域绘制矩形填充
start_index = 4853
end_index = start_index+5
# 最上边多边形框的位置偏移
poly1_offset_x = 0
poly1_offset_y = -8

fill_poly = False  # False 代表只显示边框，不实际填充 or True 代表实际填充
pics_file_path = 'pics'
pic_ends = '.jpg'
pic_save_path = 'chedPics'
test_color = (255, 255, 0)


if not os.path.exists(pic_save_path):
    os.makedirs(pic_save_path)


# 绘制上部白色胶带矩形框
def paint_poly1(frame):
    a = np.array([[[419, 599], [405, 654], [652, 715], [660, 653]]], dtype=np.int32)
    a_temp = a.reshape(4, 2)
    a_temp[:, 0] += poly1_offset_x
    a_temp[:, 1] += poly1_offset_y
    a = a_temp.reshape(1, 4, 2)
    color1 = (0, 2, 3)
    # 绘制矩形，如果thickness为负值代表填充，如果是正值则绘制矩形框
    cv2.polylines(frame, a, isClosed=True, color=test_color, thickness=1)
    if fill_poly:
        cv2.fillPoly(frame, a, color=color1)


while start_index <= end_index:
    pic = cv2.imread(os.path.join(pics_file_path, str(start_index) + pic_ends))
    paint_poly1(pic)
    pic_resize = cv2.resize(pic,(0,0),fx=0.5,fy=0.5)
    cv2.imshow('index: ' + str(start_index), pic_resize)
    cv2.waitKey(0)
    if fill_poly:
        cv2.imwrite(os.path.join(pic_save_path, str(start_index) + pic_ends), pic)

    start_index += 1
