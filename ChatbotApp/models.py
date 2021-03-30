from django.db import models

# Create your models here.

class Chat(models.Model):
    # 문자로 구성되어있는 항목
    msg =models.CharField(max_length=100)
    # 날짜
    date = models.DateTimeField()
