import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("错误，摄像头无法打开")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mohu = cv2.GaussianBlur(gray_img, (5, 5), 0)

        mean_val = np.mean(mohu)
        low_thresh = max(30, mean_val * 0.5)
        high_thresh = max(100, mean_val * 1.5)

        canny = cv2.Canny(gray_img, low_thresh, high_thresh)

        '''kernel = np.ones((3, 3), np.uint8)
        canny_clean = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
        canny_clean = cv2.morphologyEx(canny_clean, cv2.MORPH_OPEN, kernel)'''

        cv2.imshow("original", frame)
        cv2.imshow("edge", canny)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

'''    
    img = cv2.imread("D:\\.vscode\\OpenCV\\test_1.jpg", cv2.IMREAD_COLOR)

    img = cv2.resize(img, None, fx=0.5, fy=0.5)

    if img is None:
        print("未读取到图像")
    else:
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)  

    thresh1 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, C=3, blockSize=19)

    kernel = np.ones((15, 15), np.uint8)
    thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel, iterations=2)#形态学闭运算

    contours, hiearchies = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    thresh_2 = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR)

    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        zhouchang = cv2.arcLength(cnt, True)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(thresh_2, (x, y), ((x + w), (y + h)), (0, 255, 0), 2)
        cv2.putText(thresh_2, f"area:{area}, length:{zhouchang:.4f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    cv2.imshow("box", thresh_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

'''ret, thresh1 = cv2.threshold(gray_img, 110, 255, cv2.THRESH_BINARY)

    ret, thresh2 = cv2.threshold(gray_img, 110, 255, cv2.THRESH_BINARY_INV)

    ret, thresh3 = cv2.threshold(gray_img, 110, 255, cv2.THRESH_TRUNC)

    adaptive_thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 
                                            blockSize=11, C=2)
    
    canny_edges = cv2.Canny(gray_img, threshold1=100, threshold2=200)

    plt.figure(figsize=(15, 10))
    plt.subplot(2, 3, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Gray")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(thresh1, cmap="gray")
    plt.title("THRESH_BINARY")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(thresh2, cmap="gray")
    plt.title("THRESH_BINARY_INV")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.imshow(thresh3, cmap="gray")
    plt.title("THRESH_TRUNC")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.imshow(adaptive_thresh, cmap="gray")
    plt.title("Adaptive Threshold")
    plt.axis("off")

    plt.subplot(2, 3, 6)
    plt.imshow(canny_edges, cmap="gray")
    plt.title("Canny Edges")
    plt.axis("off")

    plt.show()'''

'''
    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(rgb_img)
    plt.title("rgb")
    plt.axis("off")
    plt.subplot(2, 2, 2)
    plt.imshow(gray_img)
    plt.subplot(2, 2, 3)
    plt.imshow(hsv_img)

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original (BGR→RGB)")
    plt.axis("off")
'''
'''img = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.line(img, (100, 100), (200, 100), (155, 100, 100), 4)
cv2.rectangle(img, (300, 300), (400, 400), (189, 200, 0), -1)
cv2.circle(img, (400, 50), 50, (167, 89, 90), 1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "hello", (50, 400), font, 1.2, (255, 255, 0), 2)

cv2.imshow("IMG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''img = cv2.imread("D:\\.vscode\\OpenCV\\blue_background.png", cv2.IMREAD_COLOR)
if img is None:
    print("图片读取失败")
else:
    cv2.imshow("Orignal Image", img)
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width, channels = img.shape
    pixel_count = img.size
    dtype = img.dtype
    print(f"图片高{height}, 宽{width}, 通道数{channels}, 总像素{pixel_count}, 类型为{dtype}")
    img_resize = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_BITS)
    cv2.imshow("resize", img_resize)
    flip = cv2.flip(img_resize, flipCode=-1)
    cv2.imshow("flip", flip)

    row, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, row / 2), 90, 1.0)
    r_img = cv2.warpAffine(img, M, (row, cols))
    cv2.imshow("zhuan", r_img)
    cv2.imwrite("Gray_Image.jpg", grey_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''