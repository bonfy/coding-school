# -*- coding:utf-8 -*-

###
# Author: bonfy
# Email: foreverbonfy@163.com
# Created Date: 2018-01-30
###
# coding: utf-8

import pika
import json
import os

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

message = dict(message='hello', status=200)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json.dumps(message),
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print(" [x] Sent 'Hello World!'")

connection.close()
