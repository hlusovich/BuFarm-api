"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from address.views import AddressViewSet
from comment.views import CommentViewSet
from product.views import ProductViewsSet, OrderedproductViewSet
from user.views import UserViewSet
from order.views import OrderViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'addresses',AddressViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'orderedproduct',OrderedproductViewSet)

router.register(r'product',ProductViewsSet)
router.register(r'orderstatus',OrderViewSet)

urlpatterns = router.urls#почитать Грабар не помнит#
urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),


    url(r'^api-token-verify/', verify_jwt_token),
]





