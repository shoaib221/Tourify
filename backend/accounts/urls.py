
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path('register/', views.MyRegister.as_view(), name='register'),
    # path('login/', views.MyLogin.as_view(), name='login'),
    # path('logout/', views.MyLogout.as_view(), name='logout'),
    # path("profile/<int:user_id>/", views.ShowProfileDetail.as_view()),
    # path('my_profile/', views.MyProfile.as_view(), name='profile'),
    # path("home/", views.MyHome.as_view() ),
    # path("update_name/", views.UpdateName.as_view() ),
    # path("update_mail/", views.UpdateEmail.as_view() ),
    # path("update_mobile/", views.UpdateMobile.as_view() ),
    # path( "change_password/", views.ChangePassword.as_view() ),
    # path( "forgot_password/", views.ForgotPassword.as_view(), name='forgot password'),
    # path("test/", views.Test.as_view(), name="test")

    path('test/' , views.Test.as_view() , name='test' ),
    path('register/', views.MyRegister.as_view(), name='api register'),
    path('my_profile/', views.MyProfile.as_view(), name='profile'),
    path( "login/", TokenObtainPairView.as_view()),
    path( "token-refresh/", TokenRefreshView.as_view() ),
    path( "google-login/", views.GoogleLogin.as_view(), name="google-login" )
]



# 5. Login

# Send a POST request to:

# POST /api/token/

# Body:

# {
#     "username": "shoaib",
#     "password": "12345678"
# }

# Response:

# {
#     "refresh": "eyJhbGciOi...",
#     "access": "eyJhbGciOi..."
# }
# 6. Use the access token

# React sends:

# GET /api/profile/

# Authorization: Bearer <access_token>


# 8. Refresh an expired access token

# POST:

# /api/token/refresh/

# Body:

# {
#     "refresh": "<refresh_token>"
# }

# Response:

# {
#     "access": "<new_access_token>"
# }
