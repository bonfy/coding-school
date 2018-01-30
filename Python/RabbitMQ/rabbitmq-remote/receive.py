# -*- coding:utf-8 -*-


###
# Author: bonfy
# Email: foreverbonfy@163.com
# Created Date: 2018-01-30
###


# coding: utf-8

import pika
import os
import time
import json

user = os.environ.get('USER')
pwd = os.environ.get('PASSWORD')
url = os.environ.get('URL')

credentials = pika.PlainCredentials(user, pwd)
parameters = pika.ConnectionParameters(url,
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
    # print(type(ch), ch)
    # print(type(method), method)
    # print(type(properties), properties)
    try:
        msg = json.loads(body)
        if msg.get('status') == 400:
            raise Exception('Exception occur!')
        print(" [x] Received %r" % msg)
    except Exception as e:
        print('{} Exception: {}'.format(body, e))


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
