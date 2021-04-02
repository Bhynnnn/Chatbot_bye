from django.db import models

# Create your models here.

class Member(models.Model):
    # 필요한 것
    # 이름, id학번, 학과, pw, pw확인, email

    userName = models.CharField(max_length=10, verbose_name='이름')
    userID = models.CharField(max_length=10, verbose_name='학번(ID)')
    # userMajor =
    userPassword = models.CharField(max_length=100, verbose_name='pw')
    userEmail = models.EmailField(max_length=100, verbose_name='이메일')

    def __str__(self):
        return self.userName
    #이 함수는 admin페이지에서 User object 대신 나타낼 문자자

    class Meta:
        db_table = 'user_db'


