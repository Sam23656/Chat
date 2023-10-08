from django.urls import path

from Chat_app.views import *

urlpatterns = [
    path('', show_index_page, name='index'),
    path('logout/', LogOutViewPage.as_view(), name='logout'),
    path('register/', RegisterViewPage.as_view(), name='register'),
    path('login/', LoginViewPage.as_view(), name='login'),
]
