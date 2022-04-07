# import asyncio
# import json
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
# from channels.db import database_sync_to_async
# from .models import Post


# class PostConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("connected", event)
#         await self.send({
#             "type": "websocket.accept"
#         })

#         me = self.scope['user']


#         await asyncio.sleep(3)
#         await self.send({
#             "type": "websocket.send",
#             "text": "Hello world"
#         })

#     async def websocket_receive(self, event):
#         print("receive", event)
#         front_text = event.get('text', None)
#         if front_text is not None:
#             loaded_dict_data = json.loads(front_text)
#             msg = loaded_dict_data.get('message')
#             print(msg)                                                              
    
#     async def websocket_disconnect(self, event):
#         print("disconnected", event)
        

    
# class PostLikeConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("connect", event)
    
#     async def websocket_receive(self, event):
#         print("receive", event)
    
#     async def websocket_disconnect(self, event):
#         print("disconnect", event)