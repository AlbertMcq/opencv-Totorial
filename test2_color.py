# OpenCV 颜色通道分离与灰度转换示例
import cv2

# 读取彩色图像
image = cv2.imread("opencv_logo.jpg")

# 分离并显示三个颜色通道
# OpenCV 使用 BGR 格式（蓝、绿、红），而不是常见的 RGB
# [:,:,0] 表示所有行、所有列、第0个通道（蓝色）
cv2.imshow("blue", image[:,:,0])
# [:,:,1] 表示第1个通道（绿色）
cv2.imshow("green", image[:,:,1])
# [:,:,2] 表示第2个通道（红色）
cv2.imshow("red", image[:,:,2])
# 等待按键关闭颜色通道窗口
cv2.waitKey()

# 将彩色图像转换为灰度图
# COLOR_BGR2GRAY 会根据人眼感知权重计算：Gray = 0.299*R + 0.587*G + 0.114*B
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 显示灰度图像
cv2.imshow("gray", gray)
# 等待按键关闭窗口
cv2.waitKey()