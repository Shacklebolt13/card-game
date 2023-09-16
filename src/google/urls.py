from .apis import GoogleLoginApi, GoogleLoginRedirectApi
from django.urls import path

urlpatterns = [
    path("callback/", GoogleLoginApi.as_view(), name="callback-sdk"),
    path("redirect/", GoogleLoginRedirectApi.as_view(), name="redirect-sdk"),
]
