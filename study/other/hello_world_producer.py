# -*- coding: UTF-8 -*-
import pika,sys
# 1.建立代理服务器连接
credentials = pika.PlainCredentials("guest","guest")
conn_parmas=pika.ConnectionParameters("localhost",
                                      credentials=credentials)
conn_broker=pika.BlockingConnection(conn_parmas)
# 2.获得信道
channel = conn_broker.channel()
# 3.声明交换器
channel.exchange_declare(exchange="hello-exchange",
                         type="direct",
                         passive=False,
                         durable=True,
                         auto_delete=False)
# 4.创建文本
msg = sys.argv[1]
msg_props = pika.BasicProperties
msg_props.content_type="text/plain"
# 5.发布消息
channel.basic_publish(body=msg,
                      exchange="hello-exchange",
                      properties=msg_props,
                      routing_key="hola")
