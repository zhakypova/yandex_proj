from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.views import AuthorRegisterView
from post.views import PostListCreateAPIView

account_router = DefaultRouter()
account_router.register('register', AuthorRegisterView)

post_router = DefaultRouter()
post_router.register('post', PostListCreateAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/post/', include('post.urls')),
]
