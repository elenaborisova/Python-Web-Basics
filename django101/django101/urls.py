from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django102.urls')),
    path('todos/', include('todos_app.urls')),
    path('books/', include('books.urls')),
    path('profiles/', include('testing.urls')),
]
