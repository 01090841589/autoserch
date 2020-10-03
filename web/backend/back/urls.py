from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view()),
    path('users/', views.join),
    path('users/join/<int:pk>/', views.usersPostview.as_view()),
    path('users/join/', views.usersPostview.as_view()),
    path('users/<int:pk>/', views.user_detail),
    path('login/', views.login),
    path('cars/', views.car),
    path('cars/<int:num>/', views.car_datail),
    path('cars/company/<str:company>/', views.car_company_list),
    path('cars/name/<str:name>/', views.car_name_list),
    path('cars/companyAll/', views.car_companyAll),
    path('likecarAll/', views.likecarAll),
    path('likecarUser/<int:pk>/', views.likecarUser),
    path('likecar/', views.likecar),
    path('cars/detailAi/', views.detailAI),
    #   path('like/all/', views.like_all)
    # path('cars/company_list/', views.car_companyAll)
]
