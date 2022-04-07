# import json
# from channels.consumer import AsyncConsumer
# from asgiref.sync import async_to_sync

# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         self.room_group_name = "text"
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
        # print("connect", event)
        # await self.send({
        #     "type": "websocket.accept",
        #     "text": "connect please"
        # })

    # async def websocket_receive(self, event):
    #     print("receive", event)
    #     received_data = json.loads(event['text'])
    #     msg = received_data.get("message")

    #     async_to_sync(self.channel_layer.group_send)(
    #        self.room_group_name,{
    #             'type':'chat_message',
    #         'message': msg                                                                                                                                                                                                                                                                  quit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    #         }
    #     )

    # def chat_message(self, event):
    #     message = event['message']

    #     self.send(text_data=json.dumps({ 
    #         type: 'chat',
    #         'message': message
    #     }))

        # if not msg:
        #     return False

        # response = {
        #     "message": msg
        # }

        # await self.send({
        #     "type": "websocket.send",
        #     "text": json.dumps(response)
        # })


    # async def websocket_disconnect(self, event):
    #     print("disconnect", event)

    