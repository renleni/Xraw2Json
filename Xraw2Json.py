import numpy as np
import matplotlib.pyplot as plt
import os
import json
# plt支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# raw数据读取,分别提取出低能本底数据，高能本底数据，低能满载数据，高能满载数据
def read_data(file_path , detector_num, single_channel = False):
    # 获取文件大小
    file_size = os.path.getsize(file_path)
    # 根据文件大小计算offset
    if single_channel == True:
        offset = file_size - 400 * detector_num * 64 * 2 
    else:
        offset = file_size - 400 * detector_num * 64 * 2 * 2
    img = np.fromfile(file_path, dtype=np.uint16, offset = offset) 
    if single_channel == False:
        img_width = int((file_size - offset) // 400 // 2)
        # 计算图像大小
        img = img.reshape((400, img_width))
        img_low_base = img[0:199, : img_width // 2]
        img_high_base = img[0:199, img_width // 2:]
        img_low_full = img[200:400, :img_width // 2]
        img_high_full = img[200:400,img_width // 2 :]
        return img_low_base, img_high_base, img_low_full, img_high_full
    else:
        img_width = int((file_size - offset) // 400 // 2)
        # 计算图像大小
        img = img.reshape((400, img_width))
        img_low_base = img[0:199, :]
        img_low_full = img[200:400, :]
        return img_low_base, img_low_full
# 按照计算每列数据的平均值，并输出
def calculate_mean(img):
    mean_list = []
    for i in range(img.shape[1]):
        mean_list.append(np.mean(img[:, i]))
    return mean_list

if __name__ == '__main__':
    # 读取文件夹下面的所有文件，并绘制图像
    file_folder = "./TEST"
    file_list = os.listdir(file_folder)
    single_channel = True
    detector_num = 7
    # 绘制图像，并都在一个图像中展示
    plt.figure(figsize=(10, 6))
    # 保存每个文件对应的数据
    for file_name in file_list:
        file_path = os.path.join(file_folder, file_name)
        if single_channel == False:
            img_low_base, img_high_base, img_low_full, img_high_full = read_data(file_path , detector_num , single_channel )
            mean_low_base = calculate_mean(img_low_base)
            mean_high_base = calculate_mean(img_high_base)
            mean_low_air = calculate_mean(img_low_full)
            mean_high_air = calculate_mean(img_high_full)
            mean_low_air_block = [np.mean(mean_low_air[i * 64: (i + 1) * 64]) for i in range(detector_num)]
            mean_high_air_block = [np.mean(mean_high_air[i * 64: (i + 1) * 64]) for i in range(detector_num)]
            plt.plot(mean_low_air, label=file_name)
            plt.plot(mean_high_air, label=file_name)
        else:
            img_low_base, img_low_full = read_data(file_path , detector_num , single_channel )
            mean_low_base = calculate_mean(img_low_base)
            mean_low_air = calculate_mean(img_low_full)
            mean_low_air_block = [np.mean(mean_low_air[i * 64: (i + 1) * 64]) for i in range(detector_num)]
            mean_low_air[190] = 7500
            plt.plot(mean_low_air, label=file_name)
        # 添加图例
        plt.legend()
        # X轴上每个值都画出虚线
        # plt.vlines(np.arange(0, 64 * (detector_num + 1), 64), 0, 65535, linestyles='dashed')
        plt.show()

