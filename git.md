## git tutorial
- git创建远程仓库并上传代码到远程仓库中.https://blog.csdn.net/liuweixiao520/article/details/78971221

```

git push -u origin master
 
由于新建的远程仓库是空的，所以要加上-u这个参数，等远程仓库里面有了内容之后，下次再从本地库上传内容的时候只需下面这样就可以了：

git push origin master

git pull --rebase origin master

 
```