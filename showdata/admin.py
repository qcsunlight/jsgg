from django.contrib import admin

# Register your models here.
from showdata.models import Data, DeviceName, ImportData
from showdata.utils import import_data


class DataAdmin(admin.ModelAdmin):
    list_display = ['addr', 'name', 'time', 'shui_1', 'wen_1', 'shui_2', 'wen_2', 'shui_3', 'wen_3']


class DeviceNameAdmin(admin.ModelAdmin):
    list_display = ['addr', 'name']


class ImportDataAdmin(admin.ModelAdmin):
    list_display = ['file']
    list_filter = ['file',]

    def save_model(self, request, obj, form, change):
        # re = super(ImportDataAdmin, self).save_model(request, obj, form, change)
        # obj.file = request.FILES.get('file', '')
        # import_data(self, request, obj, change)
        # return re
        re = super().save_model(request, obj, form, change)
        # print(obj.file.path)
        import_data(self, request, obj, change)
        return re

admin.site.register(Data, DataAdmin)
admin.site.register(DeviceName, DeviceNameAdmin)
admin.site.register(ImportData, ImportDataAdmin)