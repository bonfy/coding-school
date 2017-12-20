# RabbitMQ

## 安装

```cmd
$ brew install rabbitmq
$ brew services start rabbitmq
```

管理界面: http://localhost:15672/ 初始用户名密码: guest: guest

教程 [https://www.rabbitmq.com/getstarted.html](https://www.rabbitmq.com/getstarted.html)

中文文档 [http://rabbitmq.mr-ping.com/](http://rabbitmq.mr-ping.com/)

## AMQP协议

### AMQP (Advanced Message Queuing Protocol)

publisher -> (exchange) -> queue -> consumer

比传统的多了层 exchage

### 四种exchange:

* Direct exchange（直连交换机）  - (Empty string) and amq.direct
* Fanout exchange（扇型交换机）  - amq.fanout
* Topic exchange（主题交换机）   - amq.topic
* Headers exchange（头交换机)   - amq.match (and amq.headers in RabbitMQ)

除交换机类型外，在声明交换机时还可以附带许多其他的属性，其中最重要的几个分别是：

* Name
* Durability （消息代理重启后，交换机是否还存在）
* Auto-delete （当所有与之绑定的消息队列都完成了对此交换机的使用后，删掉它）
* Arguments（依赖代理本身）

交换机可以有两个状态：持久（durable）、暂存（transient）。持久化的交换机会在消息代理（broker）重启后依旧存在，而暂存的交换机则不会（它们需要在代理再次上线后重新被声明）。然而并不是所有的应用场景都需要持久化的交换机。



## Hello World

