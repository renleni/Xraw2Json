import os
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
# 拼接xraw数据

# 使用示例
folder_path = "./"
