from django.urls import path
from .views import PostsList, PostDetail, PostCreate, RespondCreate, RespondAccept
from .views import respond_accept, respond_delete, subscribe, unsubscribe


urlpatterns = [
    path('', PostsList.as_view(), name='posts_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/respond/', RespondCreate.as_view(), name='respond_create'),
    path('<int:pk>/accept/', RespondAccept.as_view(), name='respond_accept'),
    path('<int:pk>/set_accept/', respond_accept),
    path('<int:pk>/set_delete/', respond_delete),
    path('subscribe/', subscribe),
    path('unsubscribe/', unsubscribe),
]






















