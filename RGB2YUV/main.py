import numpy as np


def read_bmp(file_path):
    with open(file_path, 'rb') as f:
        # 读取BMP文件头信息
        bmp_header = f.read(54)
        width = int.from_bytes(bmp_header[18:21], byteorder='little')
        height = int.from_bytes(bmp_header[22:25], byteorder='little')
        bmp_data = np.fromfile(f, dtype=np.uint8)
    return bmp_header, bmp_data.reshape((height, width, 3))


def write_bmp(file_path, bmp_header, bmp_data):
    with open(file_path, 'wb') as f:
        # 更新文件头中的图像大小信息
        height, width, _ = bmp_data.shape
        bmp_header_updated = bmp_header[:18] + width.to_bytes(4, byteorder='little') + height.to_bytes(4,
                                                                                                       byteorder='little') + bmp_header[
                                                                                                                             26:]
        f.write(bmp_header_updated)
        bmp_data.tofile(f)


def rgb_to_yuv(rgb):
    # RGB到YUV的转换矩阵
    yuv_matrix = np.array([[0.299, 0.587, 0.114], [-0.14713, -0.28886, 0.436], [0.615, -0.51499, -0.10001]])
    yuv = np.dot(rgb.astype(np.float), yuv_matrix.T)
    yuv[:, :, 1:] += 128
    return yuv.astype(np.uint8)


def yuv_to_rgb(yuv):
    # YUV到RGB的转换矩阵
    rgb_matrix = np.array([[1, 0, 1.13983], [1, -0.39465, -0.58060], [1, 2.03211, 0]])
    yuv[:, :, 1:] -= 128
    rgb = np.dot(yuv.astype(np.float), rgb_matrix.T)
    return np.clip(rgb, 0, 255).astype(np.uint8)


def convert_rgb_to_yuv_and_save(input_file, output_file):
    bmp_header, rgb_data = read_bmp(input_file)
    yuv_data = rgb_to_yuv(rgb_data)
    write_bmp(output_file, bmp_header, yuv_data)


# 示例用法
convert_rgb_to_yuv_and_save("figure/input_rgb.bmp", "figure/output_yuv.bmp")
