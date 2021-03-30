from django.contrib import admin

# Register your models here.
# 현재 경로의 models 에서 클래스 Member 를 불러온다.
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    # 관리자 페이지에 보이게 하기
    list_display = ('userName', 'useremail', 'userPW', 'userID')

# 관리자 페이지에 등록하기
admin.site.register(Member, MemberAdmin)