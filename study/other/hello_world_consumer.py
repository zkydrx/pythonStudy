# -*- coding: UTF-8 -*-
import pika
# 有待考究，现在报错：self.async = None
# 1.建立代理服务器连接
credentials = pika.PlainCredentials("guest","guest")
conn_parms=pika.ConnectionParameters("localhost",
                                     credentials=credentials)
conn_broker=pika.BlockingConnection(conn_parms)
# 2.获得信道
channel = conn_broker.channel()
# 3.声明交换器
channel.exchange_declare(exchange="hello=exchange",
                         type="direct",
                         passive=False,
                         durable=True,
                         auto_delete=False)
# 4.声明队列
channel.queue_declare(queue="hello-queue")
# 5.通过键"hola"将队列和交换器绑定起来
channel.queue_bind(queue="hello-queue",
                   exchange="hello-exchange",
                   routing_key="hola")
# 6.用户处理传入消息的函数
def msg_consumer(channel,method,header,body):
    # 7.消息确认
    channel.basic_ack(delivery_tag=method.delivery_tag)
    # 8.停止消费并退出
    if body=="quit":
        channel.basic_cancel(consumer_tag="hello-consumer")
        channel.stop_consuming()
    else:
        print(body)
    return
# 9.订阅消费者
channel.basic_consume(msg_consumer,
                      queue="hello-queue",
                      consumer_tag="hello-consumer")
# 10.开始消费
channel.start_consuming()
