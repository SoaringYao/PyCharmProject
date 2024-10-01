# LR_10(X4, QF=10)

用Python和OpenCV实现将PNG图像按照压缩因子为10的质量进行压缩，并对图像进行4倍下采样

## 代码说明：
1. **`compress_and_downsample_image` 函数**：这个函数会对输入的 PNG 图像进行 4 倍下采样，并使用质量因子为 10 的 JPEG 格式保存压缩后的图像。
2. **`process_images_in_folder` 函数**：这个函数会遍历指定文件夹中的所有 PNG 图像，并调用 `compress_and_downsample_image` 进行处理。
3. **PNG 转为 JPEG**：由于 OpenCV 不支持设置 PNG 压缩质量，所以输出格式为 JPEG，文件名后缀也相应改变。 
4. **usage**：将 `input_images` 文件夹中的 PNG 图像按照上述方法压缩并保存到 `output_images` 文件夹中。
