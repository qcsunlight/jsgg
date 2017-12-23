from django.db import models

# Create your models here.


class Data(models.Model):
    addr = models.CharField(max_length=25, null=True, verbose_name=u'设备地址')
    name = models.CharField(max_length=25, null=True, verbose_name=u'测站名称')
    time = models.CharField(max_length=25, null=True, verbose_name=u'采集时间')
    shui_1 = models.FloatField(null=True)
    wen_1 = models.FloatField(null=True)
    shui_2 = models.FloatField(null=True)
    wen_2 = models.FloatField(null=True)
    shui_3 = models.FloatField(null=True)
    wen_3 = models.FloatField(null=True)
    # state = models.CharField(max_length=15, null=True)
    # info = models.CharField(max_length=15, null=True)
    # volt = models.CharField(max_length=15, null=True)
    # kong = models.CharField(max_length=10, null=True)
    # router = models.CharField(max_length=15, null=True)

    class Meta:
        ordering = ['addr', 'name', 'time']

    def __str__(self):
        return self.addr


class DeviceName(models.Model):
    addr = models.CharField(max_length=25, null=True, verbose_name=u'设备地址')
    name = models.CharField(max_length=25, null=True, verbose_name=u'测站名称')

    class Meta:
        ordering = ['addr', 'name']

    def __str__(self):
        return self.addr


class ImportData(models.Model):

    file = models.FileField(upload_to='File', verbose_name=u'文件')
    # name = models.CharField(max_length=60, verbose_name=u'文件名')

    class Meat:
        ordering = ['file']

    def __str__(self):
        return str(self.file)