from django.urls import path

from . import views

app_name = 'bingo'

urlpatterns = [
     path('', views.main, name='main'),
     path('big/', views.CreateMatrixView.as_view(), name='create'),
     path('small/', views.CreateMatrixViewThree.as_view(), name='create2'),
     path('matrix/', views.push_view, name='index'),
     path('matrix2/', views.push_view2, name='index2'),
     path('calculateprogressonlyservicefunction/', views.calc_progress,
          name='calc'),
     path('calculateprogressonlyservicefunction2/', views.calc_progress2,
          name='calc2'),
]
