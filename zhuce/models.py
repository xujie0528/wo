from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    passwd = models.CharField(max_length=30, verbose_name='密码')
    gender = models.BooleanField(default=False, verbose_name='性别')
    age = models.IntegerField(default=18,verbose_name='年龄')
class Meta:
    db_table = 'tb_user'
    verbose_name = '用户表'

