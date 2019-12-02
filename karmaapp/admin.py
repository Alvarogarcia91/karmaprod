from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# admin.site.register(item)
@admin.register(Block, Cilindro ,Aglutinado)
class ViewAdmin(ImportExportModelAdmin):
    pass
