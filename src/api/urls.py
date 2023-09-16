from django.urls import include, path

urlpatterns = [
    path("auth/", include(("src.authentication.urls", "authentication"))),
    path("users/", include(("src.users.urls", "users"))),
    path("errors/", include(("src.errors.urls", "errors"))),
    path("files/", include(("src.files.urls", "files"))),
]
