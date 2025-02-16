from django.contrib import admin
from .models import WebringModel
from rest_framework.authtoken.models import Token

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'url')
    search_fields = ('name', 'url')
    list_filter = ('status',)

admin.site.register(WebringModel, ParticipantAdmin)
admin.site.register(Token)