from django.contrib import admin

# Register your models here.

#Piemērs kā reģistrēt:

from .models import Article

admin.site.register(Article)
