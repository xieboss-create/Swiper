from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from common import stat
from libs.http import render_json
from userapp import logics
from userapp.forms import UserForm, ProfileForm
from userapp.models import User, Profile


def get_vcode(request):
    '''用户获取验证码'''
    phonenum = request.GET.get('phonenum')
    success = logics.send_sms(phonenum)
    if success:
        return render_json()
    else:
        return render_json(code=stat.SMS_ERR)


def submit_vcode(request):
    '''检查短信验证码，同时进行登陆或者注册'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    key = 'Vcode-%s' % phonenum
    cached_vcode = cache.get(key)
    if vcode and vcode == cached_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)  # 获取用户
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)  # 创建新用户

        # 记录用户登陆状态
        request.session['uid'] = user.id
        return render_json({'code': stat.OK, 'data': user.to_dict()})
    else:
        return JsonResponse({'code': stat.VCODE_ERR, 'data': None})


def get_profile(request):
    '''获取用户配置'''
    #get_or_create先get，没有就create
    #两个返回值
    #第一个：返回获取到的对象
    #第二个：返回值为true就创建了，false就是没有创建
    profile, _ = Profile.objects.get_or_create(id=request.uid)
    return JsonResponse({'code': stat.OK, 'data': profile.to_dict()})

def set_profile(request):
    #创建表单实例
    user_form=UserForm(request.post)
    profile_form=ProfileForm(request.post)
    # 检查数据的有效性
    if not user_form.is_valid():
        return render_json(user_form.errors,stat.USER_FORM_ERR)
    if not profile_form.is_valid():
        return render_json(profile_form.errors, stat.PROFILE_FORM_ERR)
    #保存数据
    User.objects.filter(id=request.uid).update(**user_form.cleaned_data)
    Profile.objects.filter(id=request.uid).update(**profile_form.cleaned_data)

    return render_json()