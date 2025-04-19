

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import (
    TokenError,
    InvalidToken,
    TokenBackendError,
    AuthenticationFailed,
)
class JwtMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 定义白名单路径
        white_list_prefixes = ["/user", "/user/", "user/",
                               "/permission", "/permission/",
                               "/api", "/api/course/", "/course", "/course/", "api/",
                               "/material", "/material/", "material/",
                               '/interact','/interact/', 'interact/',
                               "media/","/media/",
                               "static/","/static/",
                               # "/favicon.ico"
                               ]
        path = request.path

        # 检查路径是否以白名单前缀开头
        if any(path.startswith(prefix) for prefix in white_list_prefixes):
            # print("不需要Token验证")
            return None  # 直接放行，不需要验证

        # 检查路径是否为静态资源路径
        if path.startswith("/media") or path.startswith("/static"):
            print("静态资源路径，不需要Token验证")
            return None  # 静态资源路径直接放行

        # 需要进行Token验证的路径
        print("要进行Token验证")
        token = request.META.get("HTTP_AUTHORIZATION")
        print("Token:", token)

        if not token:
            return HttpResponse("Token缺失，请提供有效的Token！", status=401)

        try:
            # 去掉Bearer前缀并解码Token
            token = token.split(" ")[1] if " " in token else token
            AccessToken(token)  # 验证Token
        except TokenError as e:
            if "Token is invalid or expired" in str(e):
                return HttpResponse("Token过期，请重新登录！", status=401)
        except (TokenError, InvalidToken, TokenBackendError, AuthenticationFailed) as e:
            return HttpResponse(f"Token验证失败：{str(e)}", status=401)
