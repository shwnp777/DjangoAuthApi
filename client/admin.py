from django.contrib import admin
from .models import ClientModel, NotesModel

admin.site.register(ClientModel)
admin.site.register(NotesModel)
