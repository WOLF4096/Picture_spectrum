import cv2
import numpy as np
import soundfile as sf
import time

t1 = int(round(time.time() * 1000))                 #起始时间戳

img = ""    #图片路径
hz = 44100  #采样频率 hz
q = 10000   #起始频率 hz
s = 50      #频谱行距 ms
z = 10      #频谱列距 hz
            #结束频率 = 起始频率 + 图片宽度 * 频谱列距

def sin_wave(A, f, fs, phi, t):                     #生成正弦波
    Ts = 1 / fs
    n = t / Ts / 1000
    n = np.arange(n)
    y = A * np.sin(2 * np.pi * f * n * Ts + phi * (np.pi / 180))
    return y

def picture_spectrum(img ,hz ,q ,s ,z):             #生成频谱图
    img_cv = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    size = img_cv.shape
    hi = size[0]
    wi = size[1]
    data = sin_wave(0, 0, hz, 0, s)
    wave = data
    for ho in range(hi):
        for wo in range(wi):
            a = img_cv[ho][wo] / 256
            f = wo * z + q
            data = data + sin_wave(a, f, hz, a, s)
        data = data / wo
        wave = np.hstack((data,wave))
    return wave

wav = picture_spectrum(img ,hz ,q ,s ,z)
txt = str(s)+'ms_'+str(z)+'hz_'+str(t1)+'.wav'      #文件命名
sf.write(txt, wav, hz, subtype='PCM_16')            #保存wav文件

t2 = int(round(time.time() * 1000))                 #结束时间戳
t0 = '本次转换用时：' + str((t2 - t1)/1000) + 's'
print(t0)
