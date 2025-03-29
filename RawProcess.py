import os
import numpy as np

def process_raw_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"文件夹 {folder_path} 不存在")
        return
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # 获取文件大小
        file_size = os.path.getsize(file_path)
        
        # 默认图像宽度
        width = 2304
        
        # 计算图像高度
        height = file_size // (width * 2)
        
        # 构建新的文件名
        new_filename = f'xraw_{width}x{height}x2.raw'
        new_file_path = os.path.join(folder_path, new_filename)
        
        # 重命名文件,若存在相同文件名，则添加数字
        i = 1
        while os.path.exists(new_file_path):
            new_filename = f'xraw_{width}x{height}x2_{i}.raw'
            new_file_path = os.path.join(folder_path, new_filename)
            i += 1
        
        # 重命名文件
        os.rename(file_path, new_file_path)
        print(f"文件 {filename} 重命名为 {new_filename}")

# 读取xraw数据，并保存为高能数据和低能数据，然后将所有文件夹中的xraw数据的高能数据都自上而下拼接在一起，低能数据也一样
def read_data(folder_path):
    # 预定义高能最终拼接数据和低能最终拼接数据
    img_high_final = np.empty((0, 1152), dtype=np.uint16)  # 初始为空数组
    img_low_final = np.empty((0, 1152), dtype=np.uint16)   # 初始为空数组

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.startswith('xraw_'):
            with open(file_path, 'rb') as f:
                file_size = os.path.getsize(file_path)
                width = 2304
                height = file_size // (width * 2)

                img = np.fromfile(file_path, dtype=np.uint16, count=width*height)
                img = img.reshape((height, width))

                img_high = img[0:height, :1152]
                img_low = img[0:height, 1152:]
                
                # 将每个文件读取的img_high进行拼接
                img_high_final = np.concatenate((img_high_final, img_high), axis=0)
                img_low_final = np.concatenate((img_low_final, img_low), axis=0)
                
    # 将img_high_final和img_low_final进行拼接
    img_final = np.concatenate((img_high_final, img_low_final), axis=0)
    return img_final

# 使用示例
folder_path = "./"

# xraw拼接数据
img = read_data(folder_path)
img.tofile('xraw_final.raw')
