from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preassure/', include('preassureCharts.urls')),
    path('', include('pages.urls'))
]