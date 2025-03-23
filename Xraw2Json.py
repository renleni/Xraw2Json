import numpy as np
import matplotlib.pyplot as plt
import os
import json
# plt֧������
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# raw���ݶ�ȡ,�ֱ���ȡ�����ܱ������ݣ����ܱ������ݣ������������ݣ�������������
def read_data(file_path , detector_num, single_channel = False):
    # ��ȡ�ļ���С
    file_size = os.path.getsize(file_path)
    # �����ļ���С����offset
    if single_channel == True:
        offset = file_size - 400 * detector_num * 64 * 2 
    else:
        offset = file_size - 400 * detector_num * 64 * 2 * 2
    img = np.fromfile(file_path, dtype=np.uint16, offset = offset) 
    if single_channel == False:
        img_width = int((file_size - offset) // 400 // 2)
        # ����ͼ���С
        img = img.reshape((400, img_width))
        img_low_base = img[0:199, : img_width // 2]
        img_high_base = img[0:199, img_width // 2:]
        img_low_full = img[200:400, :img_width // 2]
        img_high_full = img[200:400,img_width // 2 :]
        return img_low_base, img_high_base, img_low_full, img_high_full
    else:
        img_width = int((file_size - offset) // 400 // 2)
        # ����ͼ���С
        img = img.reshape((400, img_width))
        img_low_base = img[0:199, :]
        img_low_full = img[200:400, :]
        return img_low_base, img_low_full
# ���ռ���ÿ�����ݵ�ƽ��ֵ�������
def calculate_mean(img):
    mean_list = []
    for i in range(img.shape[1]):
        mean_list.append(np.mean(img[:, i]))
    return mean_list

if __name__ == '__main__':
    # ��ȡ�ļ�������������ļ���������ͼ��
    file_folder = "./TEST"
    file_list = os.listdir(file_folder)
    single_channel = True
    detector_num = 7
    # ����ͼ�񣬲�����һ��ͼ����չʾ
    plt.figure(figsize=(10, 6))
    # ����ÿ���ļ���Ӧ������
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
        # ���ͼ��
        plt.legend()
        # X����ÿ��ֵ����������
        # plt.vlines(np.arange(0, 64 * (detector_num + 1), 64), 0, 65535, linestyles='dashed')
        plt.show()

