import json
from random import randint
import random
from time import sleep
import asyncio
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async

# CountingConsumer is a class that inherits from WebsocketConsumer
class CountingConsumer(WebsocketConsumer):
    # This is a method that is called when the consumer is ready to receive messages
    def connect(self):
        self.accept()
        # Send a message to the client
        # counting number from 0 to 100
        for i in range(0, 100):
            self.send(text_data=json.dumps({
                'message': randint(0, 100)
            }))
            sleep(1)


# User CountingConsumer is a class that inherits from WebsocketConsumer
class UserCountingConsumer(WebsocketConsumer):
    # This is a method that is called when the consumer is ready to receive messages
    def connect(self):
        self.accept()
        # Send a message to the client
       # counting users registered
        # for i in range(0, User.objects.count()):
        self.send(text_data=json.dumps({
            'message': User.objects.count()
        }))
        sleep(1)

            


# AsyncCountingConsumer is a class that inherits from AsyncWebsocketConsumer
class AsyncCountingConsumer(AsyncWebsocketConsumer):
    # This is a method that is called when the consumer is ready to receive messages
    async def connect(self):
        await self.accept()
        # Send a message to the client
        # counting number from 0 to 100
        for i in range(0, 100):
            await self.send(text_data=json.dumps({
                'message': randint(0, 100)
            }))
            await asyncio.sleep(1)


class AsyncUserCountingConsumer(AsyncWebsocketConsumer):
    # This is a method that is called when the consumer is ready to receive messages
    async def connect(self):
        await self.accept()
        # Send a message to the client
       # counting users registered
        # for i in range(0, User.objects.count()):
        await self.send(text_data=json.dumps({
            'message':  User.objects.count()
        }))
        sleep(1)