from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # User managemenn (ler rodapé!)
    path('accounts/', include('django.contrib.auth.urls')),
    # Path para efetuar login
    path("accounts/", include('accounts.urls')),
    # Path da home
    path('', include('pages.urls'))
]


"""
    ==========================================================================================================
    |               URLs incluídas por 'django.contrib.auth.urls' e seus templates associados                |
    ==========================================================================================================
    | URL                              | Nome da URL             | Template                                  |
    ----------------------------------------------------------------------------------------------------------
    | /accounts/login/                 | login                   | registration/login.html                   |
    | /accounts/logout/                | logout                  | registration/logged_out.html              |
    | /accounts/password_change/       | password_change         | registration/password_change_form.html    |
    | /accounts/password_change/done/  | password_change_done    | registration/password_change_done.html    |
    | /accounts/password_reset/        | password_reset          | registration/password_reset_form.html     |
    | /accounts/password_reset/done/   | password_reset_done     | registration/password_reset_done.html     |
    | /accounts/reset/<uidb64>/<token>/| password_reset_confirm  | registration/password_reset_confirm.html  |
    | /accounts/reset/done/            | password_reset_complete | registration/password_reset_complete.html |
    ==========================================================================================================
"""