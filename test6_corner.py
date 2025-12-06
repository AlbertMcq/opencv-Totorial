# OpenCV 角点检测示例 - Shi-Tomasi 角点检测算法
import cv2

# 读取原始图像
image = cv2.imread("opencv_logo.jpg")
# 转换为灰度图（角点检测需要在灰度图上进行）
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用 Shi-Tomasi 算法检测角点
# 参数说明：
# - gray: 输入的灰度图像
# - 500: 最多检测的角点数量
# - 0.1: 角点质量水平（0-1之间），低于这个值的角点会被丢弃
# - 10: 角点之间的最小欧氏距离，避免角点过于密集
corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)

# 遍历所有检测到的角点并标记
for corner in corners:
    # ravel() 将二维数组展平为一维，提取 x, y 坐标
    x, y = corner.ravel()
    # 在每个角点位置绘制紫色实心圆
    # 参数：图像, 圆心坐标, 半径, 颜色(BGR), 厚度(-1表示填充)
    cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)

# 显示标记了角点的图像
cv2.imshow("corners", image)
# 等待用户按任意键后关闭窗口
cv2.waitKey()