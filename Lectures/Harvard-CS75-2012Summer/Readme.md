# CS75 Harvard

> [Harvard Web Development David Malan](https://www.youtube.com/watch?v=8KuO4r5CHjM&index=1&t=854s&list=WL)


## Lecture 0

### Private Address

* 192.168.xx.xx
* 172.16.xx.xx
* 10.xx.xx.xx (这个公司，可以建好多内网地址)

### TCP/IP

* IP 定位你的主机位置
* TCP 传输数据协议 (MOVE DATA physically or electronically from Point A to point B)

HTTP: TCP 80
HTTPS: TCP 443
SMTP: TCP 25
### DNS SERVER

域名提供商 namecheap，godaddy

### NS RECORD

* A     (ip address)
* CNAME (ALIAS 别名) 比如 google.com 你的域名就会转到 google.com 然后由 google的dns告诉大家是什么ip google可以自己在里面变ip
* MX    (MAIL) 可以有多个
* NS

### 访问VPS

VPS 是现在比较多的 托管方式，其实就是  云上的 虚拟机（virtualbox， vmware之类的)

* SSH
* SFTP


### Telnet 访问 80端口

```cmd
# 端口 21
telnet www.baidu.com 

# 端口 80
# 有些不指定 host 会被禁
telnet www.baidu.com 80
GET / HTTP/1.1
Host: www.baidu.com

```

不指定 HOST 不能放回是因为 它很大可能是放在 VPS,不指定 HOST，它不知道放回哪个 `/` 网页

### nslookup

```cmd
$ nslookup harvard.edu
Server:		10.110.0.15
Address:	10.110.0.15#53

Non-authoritative answer:
Name:	harvard.edu
Address: 23.22.75.102


$ nslookup cnn.com
Server:		10.110.0.15
Address:	10.110.0.15#53

Non-authoritative answer:
Name:	cnn.com
Address: 151.101.1.67
Name:	cnn.com
Address: 151.101.65.67
Name:	cnn.com
Address: 151.101.193.67
Name:	cnn.com
Address: 151.101.129.67
```


### 修改 /etc/hosts

在最后加入这条，就会将 davidnews.com 定向到 你设置的 ip

所以...你懂的（相当于 优先级最高的 dns）

相当于 301

```
xxx.xxx.xxx.xxx  davidnews.com
```

