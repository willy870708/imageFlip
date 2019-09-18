#!/usr/bin/env python
# coding: utf-8

# In[25]:


import PIL.Image as Image
import os

#圖片位置
IMAGES_PATH = 'D:\\JupyterNotebook\\Workspace\\新增資料夾3\\' 
#圖片格式
IMAGES_FORMAT = ['.jpg']
#要拼接的小圖片大小
IMAGE_SIZE = 20 
#圖片的列數(Row)
IMAGE_ROW = 10  
#圖片的行數(Row)
IMAGE_COLUMN = 10
#圖片儲存到當前資料夾和命名
IMAGE_SAVE_PATH = 'junyi3.jpg'
 
# 資料夾中所有圖片
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]
 
# 對於參數設定與圖片數量做比對
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("圖片數量與參數不相等！")
 
# 拼接程式
def image_compose():
    #創建新圖
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))
    # 循環做拼接
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            #paste為拼接函式
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    #顯示圖片
    to_image.show()
    return to_image.save(IMAGE_SAVE_PATH) # 回傳拼接後的圖片

#使用函數
image_compose()


# In[ ]:




