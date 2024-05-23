from django.urls import path
from .views import *
urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>/', (PostDetail.as_view()),name='post'),
    path('create/', PostCreate.as_view(), name='post_create'),

    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='product_delete'),
    path('my_list/', respond_to_me, name='my_list'),
    path('<int:pk>/respond_create/', respond_create, name='respond_create'),
    path('<int:post_id>/respond_delete/<int:pk>/', respond_delete, name='respond_delete'),
    path('user_profile/<int:pk>/', UserDetail.as_view(), name='user_profile')
]