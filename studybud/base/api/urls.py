from django.urls import path
from .import views

urlpatterns =[
        path('',views.getRoutes),
       # path('api-auth/', include('rest_framework.urls')),
        path('room/<str:pk>/',views.getRoom),
        path('rooms/',views.getRooms),
]