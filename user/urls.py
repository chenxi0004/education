from django.urls import path
from user.views import (
    TokenRefreshView,
    TokenVerifyView,
    TestView,
    JwtTestview,
    LoginView,
    RegisterView,
    SaveView,
    PwdView,
    ImageView,
    AvatarView,
    SearchView,
    ActionView,
    CheckView,
    PasswordView,
    StatusView,
    GrantRole,
    Batch_grant_role,
    active_user
)

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token-verify'),
    path("test", TestView.as_view(), name="test"),
    path("jwt_test", JwtTestview.as_view(), name="jwt_test"),
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("save", SaveView.as_view(), name="save"),  # 用户添加修改
    path("updateUserPwd", PwdView.as_view(), name="updateUserPwd"),  # 修改密码
    path("uploadImage", ImageView.as_view(), name="uploadImage"),  # 头像上传
    path("updateAvatar", AvatarView.as_view(), name="updateAvatar"),  # 头像更新
    path("search", SearchView.as_view(), name="search"),  # 用户信息查询
    path("action", ActionView.as_view(), name="action"),  # 用户信息操作
    path("check", CheckView.as_view(), name="check"),  # 用户名查重
    path("resetPassword", PasswordView.as_view(), name="resetPassword"),  # 重置密码
    path("status", StatusView.as_view(), name="status"),  # 状态修改
    path("grantRole", GrantRole.as_view(), name="grant"),  # 角色授权
    path("batchGrantRole", Batch_grant_role.as_view(), name="batchGrantRole"),
    path('activate/<uidb64>/<token>/', active_user.as_view(), name='activate'),
]
