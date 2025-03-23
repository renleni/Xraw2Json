import numpy as np
import matplotlib.pyplot as plt
import os
import json
<<<<<<< HEAD
# pltæ”¯æŒä¸­æ–‡
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# rawæ•°æ®è¯»å–,åˆ†åˆ«æå–å‡ºä½èƒ½æœ¬åº•æ•°æ®ï¼Œé«˜èƒ½æœ¬åº•æ•°æ®ï¼Œä½èƒ½æ»¡è½½æ•°æ®ï¼Œé«˜èƒ½æ»¡è½½æ•°æ®
def read_data(file_path , detector_num, single_channel = False):
    # è·å–æ–‡ä»¶å¤§å°
    file_size = os.path.getsize(file_path)
    # æ ¹æ®æ–‡ä»¶å¤§å°è®¡ç®—offset
    if single_channel == True:
        offset = file_size - 400 * detector_num * 64 * 2 
    else:
        offset = file_size - 400 * detector_num * 64 * 2 * 2
    img = np.fromfile(file_path, dtype=np.uint16, offset = offset) 
    if single_channel == False:
        img_width = int((file_size - offset) // 400 // 2)
        # è®¡ç®—å›¾åƒå¤§å°
        img = img.reshape((400, img_width))
        img_low_base = img[0:199, : img_width // 2]
        img_high_base = img[0:199, img_width // 2:]
        img_low_full = img[200:400, :img_width // 2]
        img_high_full = img[200:400,img_width // 2 :]
        return img_low_base, img_high_base, img_low_full, img_high_full
    else:
        img_width = int((file_size - offset) // 400 // 2)
        # è®¡ç®—å›¾åƒå¤§å°
        img = img.reshape((400, img_width))
        img_low_base = img[0:199, :]
        img_low_full = img[200:400, :]
        return img_low_base, img_low_full
# æŒ‰ç…§è®¡ç®—æ¯åˆ—æ•°æ®çš„å¹³å‡å€¼ï¼Œå¹¶è¾“å‡º
=======

# rawÊı¾İ¶ÁÈ¡,·Ö±ğÌáÈ¡³öµÍÄÜ±¾µ×Êı¾İ£¬¸ßÄÜ±¾µ×Êı¾İ£¬µÍÄÜÂúÔØÊı¾İ£¬¸ßÄÜÂúÔØÊı¾İ
def read_xraw(file_path , detector_num, single_channel = False):
    try:
        # »ñÈ¡ÎÄ¼ş´óĞ¡
        file_size = os.path.getsize(file_path)

        # ¸ù¾İÎÄ¼ş´óĞ¡¼ÆËãoffset
        if single_channel == True:
            offset = file_size - 400 * detector_num * 64 * 2 
        else:
            offset = file_size - 400 * detector_num * 64 * 2 * 2
        
        # ¶ÁÈ¡Êı¾İ
        img = np.fromfile(file_path, dtype=np.uint16, offset = offset) 
        img_width = int((file_size - offset) // 400 // 2)
        img = img.reshape((400, img_width))

        if single_channel == False:
            img_low_base = img[0:199, : img_width // 2]
            img_high_base = img[0:199, img_width // 2:]
            img_low_full = img[200:400, :img_width // 2]
            img_high_full = img[200:400,img_width // 2 :]
            return img_low_base, img_high_base, img_low_full, img_high_full
        else:
            # ¼ÆËãÍ¼Ïñ´óĞ¡
            img = img.reshape((400, img_width))
            img_low_base = img[0:199, :]
            img_low_full = img[200:400, :]
            return img_low_base, img_low_full
    except FileNotFoundError:
        print(f"ÎÄ¼şÎ´ÕÒµ½: {file_path}")
    except Exception as e:
        print(f"¶ÁÈ¡ÎÄ¼şÊ±·¢Éú´íÎó: {e}")
    
# °´ÕÕ¼ÆËãÃ¿ÁĞÊı¾İµÄÆ½¾ùÖµ£¬²¢Êä³ö
>>>>>>> 0139a1d52dd0a3a735cff1e34abc7afc27a2dc37
def calculate_mean(img):
    mean_list = []
    for i in range(img.shape[1]):
        mean_list.append(np.mean(img[:, i]))
    return mean_list

if __name__ == '__main__':
    # è¯»å–æ–‡ä»¶å¤¹ä¸‹é¢çš„æ‰€æœ‰æ–‡ä»¶ï¼Œå¹¶ç»˜åˆ¶å›¾åƒ
    file_folder = "./TEST"
    file_list = os.listdir(file_folder)
    single_channel = True
    detector_num = 7
    # ç»˜åˆ¶å›¾åƒï¼Œå¹¶éƒ½åœ¨ä¸€ä¸ªå›¾åƒä¸­å±•ç¤º
    plt.figure(figsize=(10, 6))
    # ä¿å­˜æ¯ä¸ªæ–‡ä»¶å¯¹åº”çš„æ•°æ®
    for file_name in file_list:
        file_path = os.path.join(file_folder, file_name)
        if single_channel == False:
            img_low_base, img_high_base, img_low_full, img_high_full = read_xraw(file_path , detector_num , single_channel )
            mean_low_base = calculate_mean(img_low_base)
            mean_high_base = calculate_mean(img_high_base)
            mean_low_air = calculate_mean(img_low_full)
            mean_high_air = calculate_mean(img_high_full)
            mean_low_air_block = [np.mean(mean_low_air[i * 64: (i + 1) * 64]) for i in range(detector_num)]
            mean_high_air_block = [np.mean(mean_high_air[i * 64: (i + 1) * 64]) for i in range(detector_num)]
        else:
            img_low_base, img_low_full = read_xraw(file_path , detector_num , single_channel )
            mean_low_base = calculate_mean(img_low_base)
            mean_low_air = calculate_mean(img_low_full)
            mean_low_air_block = [np.mean(mean_low_air[i * 64: (i + 1) * 64]) for i in range(detector_num)]
<<<<<<< HEAD
            mean_low_air[190] = 7500
            plt.plot(mean_low_air, label=file_name)
        # æ·»åŠ å›¾ä¾‹
        plt.legend()
        # Xè½´ä¸Šæ¯ä¸ªå€¼éƒ½ç”»å‡ºè™šçº¿
        # plt.vlines(np.arange(0, 64 * (detector_num + 1), 64), 0, 65535, linestyles='dashed')
        plt.show()

=======
            mean_low_air[190] = 7500
>>>>>>> 0139a1d52dd0a3a735cff1e34abc7afc27a2dc37
