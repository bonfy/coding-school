# Mac安装 Centos 7 虚拟机

> 记录下自己安装 Centos 虚拟机的过程

参考: 

* [http://www.zkt.name/macshang-shi-yong-virtualboxxu-ni-centos/](http://www.zkt.name/macshang-shi-yong-virtualboxxu-ni-centos/)
* [https://unix.stackexchange.com/questions/121588/cant-access-ssh-in-my-vm-centos](https://unix.stackexchange.com/questions/121588/cant-access-ssh-in-my-vm-centos)

## 装机

virtualbox

```cmd
brew cask install virtualbox
```

下载好CentOS7 Minimal(下载链接)的ISO镜像之后，就开始系统的安装(我的VirtualBox是英文版），步骤如下：

1. 打开VirtualBox点击左上角的 New新建，填入Name、Tyepe(Linux)、Version(Red Hat(64-bit)),Continue
2. 设置Memory size，这里我设置为1024M就够了，Continue
3. 设置Hard disk，默认(Create a virtual hard disk now)，Create
4. 设置Hard disk file type，默认(VDI)，Continue
5. 设置Storage on physical hard disk，默认(Dynamically allocated)，Continue
6. 设置File location and size， 默认位置，磁盘大小设为8G，Create
7. 设置完成点击Start启动虚拟机，这时候弹框需要输入一个系统镜像，选择之前下载完成的CentOS镜像文件路径，点Start开始安装。

安装过程很简单，系统安装位置选默认分区点一下，进行下一步进行安装，安装时间会比较长，过程中设置root密码，是否创建新用户由自己决定。

系统安装好之后点击重启，进入系统出现黑框要求输入登录账号和密码，系统就装好了。


## 访问外网

```cmd
$ vi /etc/sysconfig/network-scripts/ifcfg-enp0s3

# 修改 ONBOOT=yes
```

这样虚拟机 可以访问 外网


## SSH

就是建立 127.0.0.1:2222 -》 10.0.2.15:22
```cmd
$ VBoxManage modifyvm "CentOS" --natpf1 "SSH,tcp,127.0.0.1,2222,10.0.2.15,22" 

$ ssh root@127.0.0.1
```
