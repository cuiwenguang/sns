from django.contrib import admin
from .models import Channel
# Register your models here.


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['id', 'channel_name', 'order_index']

admin.site.register(Channel,ChannelAdmin)