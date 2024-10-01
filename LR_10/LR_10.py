import cv2
import os


def compress_and_downsample_image(input_image_path, output_image_path, quality_factor=10):
    # 读取图片
    image = cv2.imread(input_image_path)

    # 确保图像正确读取
    if image is None:
        print(f"Error: Could not read image {input_image_path}")
        return

    # 获取图片尺寸
    height, width = image.shape[:2]

    # 对图像进行 4 倍下采样
    downsampled_image = cv2.resize(image, (width // 4, height // 4), interpolation=cv2.INTER_AREA)

    # 将图像以指定的质量因子进行压缩保存
    # cv2.imwrite 不支持直接指定压缩质量的PNG文件，所以我们使用 JPEG 格式
    # 使用图像压缩函数，将下采样图像压缩为JPEG格式并设置压缩质量
    compression_params = [cv2.IMWRITE_JPEG_QUALITY, quality_factor]

    # 将下采样后的图像保存为 JPEG 格式
    output_image_path_jpg = output_image_path.replace('.png', '.jpg')
    cv2.imwrite(output_image_path_jpg, downsampled_image, compression_params)

    print(f"Compressed and downsampled image saved as: {output_image_path_jpg}")


# 处理文件夹中的所有图片
def process_images_in_folder(input_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的所有图片
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            compress_and_downsample_image(input_image_path, output_image_path)


# 示例用法
input_folder = 'DF2K_HR'  # 输入图片的文件夹
output_folder = 'LR_10'  # 输出图片的文件夹

process_images_in_folder(input_folder, output_folder)
