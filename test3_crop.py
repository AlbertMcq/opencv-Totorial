# OpenCV 图像裁剪示例
import cv2

# 读取原始图像
image = cv2.imread("opencv_logo.jpg")

# 使用数组切片裁剪图像
# 格式：image[行起始:行结束, 列起始:列结束]
# [10:170, 40:200] 表示裁剪从第10行到第170行，从第40列到第200列的区域
crop = image[10:170, 40:200]

# 显示裁剪后的图像
cv2.imshow("crop", crop)
# 等待用户按任意键后关闭窗口
cv2.waitKey()