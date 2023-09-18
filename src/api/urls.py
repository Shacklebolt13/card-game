from django.urls import include, path

urlpatterns = [
    path("users/", include(("src.users.urls", "users"))),
    path("files/", include(("src.files.urls", "files"))),
    path("auth/", include(("src.authentication.urls", "authentication"))),
    path("oauth2/", include(("src.google.urls", "oauth2"))),
]
