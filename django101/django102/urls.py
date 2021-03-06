from django.urls import path
from django102.views import index as index_view, UsersListView, GamesListView, something, methods_demo

urlpatterns = [
    path('', index_view),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('smth/', something),
    path('methods/', methods_demo),
]
