from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from common import stat


class AuthMiddleware(MiddlewareMixin):
    white_list=(
        '/api/user/get_vcode',
        '/api/user/submit_vcode',
    )
    def process_request(self,request):
        # 检查当前请求的路径是否在 白名单 中
        if request.path in self.white_list:
            return
        uid=request.session.get('uid')
        if not uid:
            return JsonResponse({'code': stat.LOGIN_REQUIRED, 'data': None})
        else:
            request.uid = uid
