import cv2
import os
import numpy as np

def resize(img, size):
    """Resize ảnh về kích thước mới."""
    img = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    return img
    
def reduce_noise(img, kernel_size=5):
    """Khử nhiễu ảnh bằng bộ lọc trung vị."""
    img = cv2.medianBlur(img, kernel_size)
    return img

def sharpen(img, alpha=9):
    """Làm sắc nét ảnh bằng bộ lọc Laplacian."""
    kernel = np.array([[-1,-1,-1], [-1,alpha,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    return img

def estimate_noise_level(img):
    """Đo độ nhiễu dựa trên phương sai Laplacian."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def estimate_sharpness(img):
    """Đo độ sắc nét dựa trên phương sai Laplacian."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def determine_kernel_size(standard_img, img):
    """Xác định kernel_size cho ảnh B dựa trên mức nhiễu của ảnh A."""
    noise_A = estimate_noise_level(standard_img)
    noise_B = estimate_noise_level(img)
    
    # Nếu B có nhiều nhiễu hơn A, dùng kernel lớn hơn để làm mịn
    if noise_B > noise_A:
        diff = min(int((noise_B - noise_A) / 10), 7)
        kernel_size = 3 + (diff if diff % 2 == 1 else diff + 1)
    else:
        kernel_size = 3

    return min(kernel_size, 9)

def determine_alpha(standard_img, img):
    """Xác định giá trị alpha phù hợp để làm sắc nét ảnh B dựa trên ảnh A."""
    sharpness_A = estimate_sharpness(standard_img)
    sharpness_B = estimate_sharpness(img)

    # Điều chỉnh alpha dựa trên mức độ sắc nét
    if sharpness_B < sharpness_A:
        diff = int((sharpness_A - sharpness_B) / 10)
        alpha = 9 + diff
    else:
        diff = int((sharpness_B - sharpness_A) / 20)
        alpha = 9 - diff

    return max(5, min(alpha, 15))

def enhance_image(standard_img, img):
    """Tăng cường chất lượng ảnh B dựa trên ảnh A."""
    kernel_size = determine_kernel_size(standard_img, img)
    alpha = determine_alpha(standard_img, img)

    img = reduce_noise(img, kernel_size)
    img = sharpen(img, alpha)

    return img


# Cách t định làm: chọn 1 ảnh làm chuẩn, sau đó chỉnh các ảnh còn lại sao cho giống ảnh chuẩn nhất có thể
# có thể chỉnh tay 1 ảnh để làm mẫu

def test():
    standard_img = cv2.imread('../data/raw_images/Archery_1.jpg')
    img = cv2.imread('../data/raw_images/Archery_2.jpg')
    img = enhance_image(standard_img, img)
    cv2.imwrite('../data/processed_images/Archery_2.jpg', img)




