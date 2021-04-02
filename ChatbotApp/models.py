from django.db import models

# Create your models here.

class Member(models.Model):
    # 필요한 것
    # 이름, id학번, pw, 학과, email

    userName = models.CharField(max_length=10, verbose_name='이름')
    userID = models.CharField(max_length=10, verbose_name='학번(ID)')
    userPassword = models.CharField(max_length=100, verbose_name='pw')
    userEmail = models.EmailField(max_length=100, verbose_name='이메일')

    def __str__(self):
        # 생성되는 객체의 타입을 문자열로 변환해서 보여주게 한다.
        # 생성된 객체가 userName 으로 보이게 된다.
        # 설정을 하지 않았을 시 object(1) 이렇게 표시된다.
        return self.userName


