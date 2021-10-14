修改 ~/.pip/pip.conf 文件，如下，添加了源并修改了默认超时时间

```
mkdir ~/.pip

vim ~/.pip/pip.conf

```

```
[global]
timeout = 6000
index-url = http://mirrors.aliyun.com/pypi/simple
[install]
trusted-host=mirrors.aliyun.com
```
