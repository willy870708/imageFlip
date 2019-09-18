#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image
import matplotlib.pyplot as plt
import cv2
import os
get_ipython().run_line_magic('matplotlib', 'inline')

#儲存照片數量的變數
i = 1
#水平平移
x = 0
#垂直平移
y = 0

for v in range(10):    
    for h in range(10):
        #手動更改讀取相片
        im = Image.open('D:\\實習\\大林慈濟\\AI相關\\200.jpg')
    
        #先水平裁減   (左,上,右,下)
        im = im.crop((x, y, x+20, y+20))        
        
        #存取照片的路徑位置
        path = "D:\\實習\\大林慈濟\\AI相關\\200\\"+str(i).zfill(3)+".jpg"
        
        #裁剪後大小顯示並儲存
        print('裁剪後大小:',im.size)
        plt.imshow(im)
        plt.show()
        im.save(path)
        #第i張照片儲存後換i+1張
        i = i+1
        #水平向右20個單位單位
        x = x+20
    #垂直向下20個單位
    y = y+20
    #水平座標從0開始，再跑一次for h in range(20)迴圈
    x = 0


# In[ ]:




