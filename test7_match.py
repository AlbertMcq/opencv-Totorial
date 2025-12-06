# OpenCV 模板匹配示例 - 在扑克牌图像中查找相同的图案
import cv2
import numpy as np

# 读取扑克牌图像
image = cv2.imread("poker.jpg")
# 将彩色图像转换为灰度图（模板匹配在灰度图上更高效）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 从灰度图中裁剪一个区域作为模板
# [行75:105, 列235:265] 提取一个 30x30 像素的区域
template = gray[75:105, 235:265]

# 使用归一化相关系数方法进行模板匹配
# TM_CCOEFF_NORMED 返回 -1 到 1 之间的值，1 表示完全匹配
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
# 找出所有匹配度大于等于 0.9（90%相似度）的位置
locations = np.where(match >= 0.9)

# 获取模板的高度和宽度，用于绘制矩形框
h, w = template.shape[0:2]
# 遍历所有匹配位置并绘制矩形框
# locations[::-1] 将 (y,x) 格式反转为 (x,y) 格式
# zip(*...) 将 x 坐标数组和 y 坐标数组配对成 (x,y) 坐标点
for p in zip(*locations[::-1]):
    # 提取矩形左上角坐标
    x1, y1 = p[0], p[1]
    # 计算矩形右下角坐标（左上角 + 模板尺寸）
    x2, y2 = x1 + w, y1 + h
    # 在原始彩色图像上绘制绿色矩形框，线条粗细为 2 像素
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 显示标注了匹配区域的图像
cv2.imshow("match", image)
# 等待用户按任意键后关闭窗口
cv2.waitKey()
