import struct

import numpy as np


# 读取BMP文件头
def read_bmp_header(file):
    header_data = file.read(54)  # 读取BMP文件头，通常是54字节
    return header_data


# 读取BMP图像数据
def read_bmp_data(file, width, height):
    pixel_array = []
    padding = (4 - (width * 3) % 4) % 4  # 计算每行的字节对齐填充
    for _ in range(height):
        row_data = []
        for _ in range(width):
            bgr_data = file.read(3)  # 读取BGR像素数据
            blue, green, red = struct.unpack("<BBB", bgr_data)  # 以小端模式解包像素数据
            row_data.append((red, green, blue))  # 注意顺序调整为(R, G, B)
        file.read(padding)  # 跳过填充字节
        pixel_array.append(row_data)
    return pixel_array


# 将RGB颜色空间转换为YUV颜色空间
def rgb_to_yuv(rgb):
    R, G, B = rgb
    m1 = np.array([R, G, B])
    m2 = np.array([[0.299, 0.587, 0.114], [-0.148, -0.289, 0.437], [0.615, -0.515, -0.100]])
    YUV = np.dot(m2, m1.T)
    Y = YUV[0]
    U = YUV[1]
    V = YUV[2]
    # Y = 0.299 * R + 0.587 * G + 0.114 * B
    # U = -0.14713 * R - 0.28886 * G + 0.436 * B
    # V = 0.615 * R - 0.51499 * G - 0.10001 * B
    return int(Y), int(U), int(V)


# 将YUV颜色空间转换为RGB颜色空间
def yuv_to_rgb(yuv):
    Y, U, V = yuv
    R = Y + 1.13983 * V
    G = Y - 0.39465 * U - 0.58060 * V
    B = Y + 2.03211 * U
    return int(R), int(G), int(B)


# 保存BMP图像文件
def save_bmp_file(header, pixel_array, filename):
    with open(filename, 'wb') as file:
        file.write(header)
        for row in pixel_array:
            for pixel in row:
                file.write(struct.pack("<BBB", *pixel[::-1]))  # 注意将(R, G, B)转换为(B, G, R)


# 主函数
def main():
    # 读取BMP文件
    with open("input_image.bmp", 'rb') as file:
        header = read_bmp_header(file)
        width, height = struct.unpack("<ii", header[18:26])
        pixel_array = read_bmp_data(file, width, height)

    # 将RGB转换为YUV
    for row in range(height):
        for col in range(width):
            pixel_array[row][col] = rgb_to_yuv(pixel_array[row][col])

    # 保存YUV图像到新文件
    save_bmp_file(header, pixel_array, "output_image_yuv.bmp")


if __name__ == "__main__":
    main()
