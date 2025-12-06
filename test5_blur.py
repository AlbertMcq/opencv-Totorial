# OpenCV 图像模糊/平滑处理示例
import cv2

# 读取原始图像
image = cv2.imread("plane.jpg")

# 高斯模糊 - 用于降噪和平滑图像
# 参数：原图像, 卷积核大小(必须是奇数), 标准差(0表示自动计算)
# (5,5) 表示使用 5x5 的高斯核，核越大模糊效果越明显
gauss = cv2.GaussianBlur(image, (5,5), 0)

# 中值模糊 - 对椒盐噪声特别有效
# 参数：原图像, 卷积核大小(必须是奇数)
# 取周围像素的中值作为当前像素值，能有效去除噪点
median = cv2.medianBlur(image, 5)

# 显示原始图像
cv2.imshow("image", image)
# 显示高斯模糊结果
cv2.imshow("gauss", gauss)
# 显示中值模糊结果
cv2.imshow("median", median)

# 等待用户按任意键后关闭所有窗口
cv2.waitKey()