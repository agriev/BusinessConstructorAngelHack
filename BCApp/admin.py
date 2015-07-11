from django.contrib import admin

# Register your models here.

from .models import BCUser,BCBusinessUnit,BCBusinessModel

admin.site.register(BCUser)
admin.site.register(BCBusinessModel)
admin.site.register(BCBusinessUnit)

