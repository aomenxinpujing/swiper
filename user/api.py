from django.shortcuts import render

# Create your views here.
# 提交手机号
def submit_phone(request):
    phonenum = request.POST.get('phone')


# 获取验证码登录注册
def submit_code(request):
    pass


# 获取个人资料
def get_profile(request):
    pass


# 修改个人资料
def edit_profile(request):
    pass


# 头像上传
def upload_icon(request):
    pass