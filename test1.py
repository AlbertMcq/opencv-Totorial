# OpenCV 基础示例 - 显示版本和读取图像
import cv2

# 打印 OpenCV 版本号
print (cv2.getVersionString())

# 读取图像文件
image = cv2.imread("opencv_logo.jpg")
# 打印图像的形状：(高度, 宽度, 通道数)
# 例如：(240, 320, 3) 表示高240像素，宽320像素，3个颜色通道(BGR)
print(image.shape)

# 在窗口中显示图像
cv2.imshow("image", image)
# 等待用户按任意键后关闭窗口
cv2.waitKey()
