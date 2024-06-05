from datetime import datetime

from django.db import models


# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(), )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Counters'  # 数据库表名


class Falans(models.Model):
    id = models.AutoField
    ## 压力
    Prssure = models.CharField(max_length=11, default=0)
    ## 通经
    Diameter = models.CharField(max_length=11, default=0)
    ## 长度
    Lenght = models.CharField(max_length=11, default=0)
    ## 外径
    OutsideDiameter = models.CharField(max_length=11, default=0)
    ## 孔中心
    Centre = models.CharField(max_length=11, default=0)
    ## 水线台阶
    WaterLineStep =  models.CharField(max_length=11, default=0)
    ## 厚度
    Thick = models.CharField(max_length=11, default=0)
    ## 水线高度
    WaterLineHeight =  models.CharField(max_length=11, default=0)
    ## 孔数量
    Count =  models.CharField(max_length=11, default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Falans'  # 数据库表名