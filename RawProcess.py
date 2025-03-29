import os
def process_raw_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"�ļ��� {folder_path} ������")
        return
    # �����ļ����е������ļ�
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # ��ȡ�ļ���С
        file_size = os.path.getsize(file_path)
        
        # Ĭ��ͼ����
        width = 2304
        
        # ����ͼ��߶�
        height = file_size // (width * 2)
        
        # �����µ��ļ���
        new_filename = f'xraw_{width}x{height}x2.raw'
        new_file_path = os.path.join(folder_path, new_filename)
        
        # �������ļ�,��������ͬ�ļ��������������
        i = 1
        while os.path.exists(new_file_path):
            new_filename = f'xraw_{width}x{height}x2_{i}.raw'
            new_file_path = os.path.join(folder_path, new_filename)
            i += 1
        
        # �������ļ�
        os.rename(file_path, new_file_path)
        print(f"�ļ� {filename} ������Ϊ {new_filename}")
# ƴ��xraw����

# ʹ��ʾ��
folder_path = "./"
