clear all;close all;clc;
load('system1_row');
for i = 1:11737    
    image1 = system1_row(1:400,i); %�Ĥ@��20*20�϶�
    image1_reshape = reshape(image1,[20,20]); %�N1*400�୼20*20
    image1_new = image1_reshape*255; %�]���쥻�ƭȦ����W��0-1�����A�]���n���^��
    image1_new = uint8(image1_new); %�W�@����ܪ��ƭȦbmatlab��type�Odouble�����A���O�n�Ʀ��Ƕ��N�n�୼uint8
    image1_flip = flip(image1_reshape,2);%�v��½��
    image1_rotation = rot90(image1_flip,1);%�v������
    image1_flip = reshape(image1_flip,[400,1]);
    temp = system2_row(401:402,i)
    system2_row(401:402,i+639) = temp;    %½�৹��[��᭱���ƶq
    system2_row(1:400,i+639) = image1_flip%½�৹��[��᭱���ƶq
end