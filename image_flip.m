clear all;close all;clc;
load('system1_row');
for i = 1:11737    
    image1 = system1_row(1:400,i); %第一個20*20區塊
    image1_reshape = reshape(image1,[20,20]); %將1*400轉乘20*20
    image1_new = image1_reshape*255; %因為原本數值有正規化0-1之間，因此要乘回來
    image1_new = uint8(image1_new); %上一行顯示的數值在matlab的type是double型式，但是要化成灰階就要轉乘uint8
    image1_flip = flip(image1_reshape,2);%影像翻轉
    image1_rotation = rot90(image1_flip,1);%影像旋轉
    image1_flip = reshape(image1_flip,[400,1]);
    temp = system2_row(401:402,i)
    system2_row(401:402,i+639) = temp;    %翻轉完後加到後面的數量
    system2_row(1:400,i+639) = image1_flip%翻轉完後加到後面的數量
end