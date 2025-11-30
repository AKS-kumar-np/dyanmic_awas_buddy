from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message, Place

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Place)
admin.site.register(Message)