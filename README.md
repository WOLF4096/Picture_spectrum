# 一种基于频谱的高质量图片传输方案

当前程序没有做多线程优化，大图转换会比较慢，在我电脑上平均 19200 像素/s  
意味着一张 1920 x 1080 的图转换成频谱需要 1920 x 1080 / 19200 = 108 s  

## 演示视频
https://www.bilibili.com/video/BV1oh4y1k7tK/
## 高质量频谱效果 
原图分辨率 1080 x 1080  
![image](https://github.com/WOLF4096/Picture_spectrum/assets/98315254/813b5e34-88c1-45f3-955f-6876542321ec)
![image](https://github.com/WOLF4096/Picture_spectrum/assets/98315254/d6d2be00-3b3e-46d0-b826-3e4d3d9cbe4e)

## 低占用频谱效果
可用于无线电传图，比SSTV还快，可自定义带宽  
最低只需占用 横向分辨率 x 2 的带宽  
例如 160 x 120 的图只需占用 320 Hz 就能看清    
![image](https://github.com/WOLF4096/Picture_spectrum/assets/98315254/19965550-f7ff-4ce9-91af-96712287d270)

