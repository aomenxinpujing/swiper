from django.core.cache import cache

from commen.error import CODE_ERROR,PROFILE_ERROR
from lib.sms import config
from lib.sms.ucpaas.sms import send_sms
from lib.transform_json import render_json
from user.forms import ProfileForm
from user.models import User


# 提交手机号
def submit_phone(request):
    phonenum = request.POST.get('phonenum')
    status, msg = send_sms(phonenum)
    return render_json(data=(status, msg))


# 获取验证码登录注册
def submit_code(request):
    code = request.POST.get('code')
    phone_num = request.POST.get('phonenum')

    cache_code = cache.get(config.FORMAT_CODE % phone_num)

    if code == cache_code:
        user,created = User.objects.get_or_create(phonenum=phone_num,
                                                  nickname=phone_num)
        request.session['uid'] = user.id
        return render_json(data=user.to_dict())
    else:
        return render_json(data='验证码错误', code=CODE_ERROR)


# 获取个人资料
def get_profile(request):
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    return render_json(user.profile.to_dict())


# 修改个人资料
def edit_profile(request):
    profileform = ProfileForm(request.POST)
    user = User.objects.get(id=request.session['uid'])
    if profileform.is_valid():
        profile = profileform.save(commit=False)
        user.profile = profile
        profile.save()
        return render_json(profile.to_dict())
    else:
        return render_json(profileform.errors, PROFILE_ERROR)


# 头像上传
def upload_icon(request):
    pass