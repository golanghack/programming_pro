import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'
        # connect to group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # connecting
        await self.accept()
    
    async def disconnect(self, close_code):
        # from out room 
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send messages in group of room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': timezone.now().isoformat(),
            }
        )
    async def char_message(self, event):
        # send message in ws 
        await self.send(text_data=json.dumps(event))