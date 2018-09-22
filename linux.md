## linux tutorial
- Ubuntu 16.04 LTS 搜狗输入法安装: https://blog.csdn.net/qq_23869697/article/details/79048238
- Ubuntu16.04下Pytorch安装(基于conda或pip)：https://blog.csdn.net/yucicheung/article/details/79094657

## userful trick

- GDebi，这个工具能够根据软件库自行解决依赖关系。
```
sudo apt-get install gdebi
sudo gdebi sogoupinyin_2.2.0.0102_amd64.deb
```
## install pytorch

首先装cuda 8.0, anaconda, 然后输入：

```
conda install pytorch torchvision cuda80 -c soumith
```