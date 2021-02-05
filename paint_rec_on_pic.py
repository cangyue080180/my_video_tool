import cv2
import os
import numpy as np

# 在图形的指定区域绘制矩形填充
start_index = 248
end_index = 250
# 最上边多边形框的位置偏移
poly1_offset_x = -28
poly1_offset_y = -10
# 中间多边形框的位置偏移
poly2_offset_x = -28
poly2_offset_y = -30
# 最下边多边形框的位置偏移
poly3_offset_x = 0
poly3_offset_y = 0

fill_poly = False  # False 代表只显示边框，不实际填充 or True 代表实际填充
has_poly3 = False  # False 代表无第三个多边形框 or True 代表有第三个多边形框
pics_file_path = 'pics'
pic_ends = '.jpg'
pic_save_path = 'chedPics'
test_color = (255, 255, 0)


if not os.path.exists(pic_save_path):
    os.makedirs(pic_save_path)


# 绘制上部白色胶带矩形框
def paint_poly1(frame):
    poly1_points_list = [[[646, 28], [659, 73], [758, 73], [758, 28]]]
    a = np.array(poly1_points_list, dtype=np.int32)
    a_temp = a.reshape(4, 2)
    a_temp[:, 0] += poly1_offset_x
    a_temp[:, 1] += poly1_offset_y
    a = a_temp.reshape(1, 4, 2)
    color1 = (193, 194, 192)
    # 绘制矩形，如果thickness为负值代表填充，如果是正值则绘制矩形框
    cv2.polylines(frame, a, isClosed=True, color=test_color, thickness=1)
    if fill_poly:
        cv2.fillPoly(frame, a, color=color1)


# 绘制下部白色胶带矩形框
def paint_poly2(frame):
    poly2_points_list = [[[578, 345], [578, 376], [607, 382], [622, 381], [699, 370], [699, 329]]]
    b = np.array(poly2_points_list, dtype=np.int32)
    b_temp = b.reshape(6, 2)
    b_temp[:, 0] += poly2_offset_x
    b_temp[:, 1] += poly2_offset_y
    b = b_temp.reshape(1, 6, 2)
    color2 = (152, 151, 153)
    # 绘制矩形，如果thickness为负值代表填充，如果是正值则绘制矩形框
    cv2.polylines(frame, b, isClosed=True, color=test_color, thickness=1)
    if fill_poly:
        cv2.fillPoly(frame, b, color=color2)


# 绘制蓝色区域多边形框
def paint_poly3(frame):
    poly3_points_list = [[[407, 527], [407, 545], [543, 522], [545, 505]]]
    c = np.array(poly3_points_list, dtype=np.int32)
    c_temp = c.reshape(4, 2)
    c_temp[:, 0] += poly3_offset_x
    c_temp[:, 1] += poly3_offset_y
    c = c_temp.reshape(1, 4, 2)
    color3 = (205, 95, 0)
    # 绘制矩形，如果thickness为负值代表填充，如果是正值则绘制矩形框
    cv2.polylines(frame, c, isClosed=True, color=test_color, thickness=1)
    if fill_poly:
        cv2.fillPoly(frame, c, color=color3)


while start_index <= end_index:
    pic = cv2.imread(os.path.join(pics_file_path, str(start_index) + pic_ends))
    paint_poly1(pic)
    paint_poly2(pic)
    if has_poly3:
        paint_poly3(pic)
    cv2.imshow('index: ' + str(start_index), pic)
    cv2.waitKey(0)
    cv2.imwrite(os.path.join(pic_save_path, str(start_index) + pic_ends), pic)

    start_index += 1
