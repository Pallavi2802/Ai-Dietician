from django.contrib import admin
from . models import AddUser,Diet,Calories,BodyMassIndex

# Register your models here.
admin.site.register(AddUser)
admin.site.register(Diet)
admin.site.register(BodyMassIndex)
admin.site.register(Calories)
