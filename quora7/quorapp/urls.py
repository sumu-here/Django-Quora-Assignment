from django.urls import path
from quorapp import views

app_name="quorapp"

urlpatterns = [
    path('',views.index ,name='index'),
    path('base/',views.base,name='base'),
    path('addquestion/',views.addquestion,name='addquestion'),    
    path('detail/<int:id>/', views.detail, name='detail'),
    path('like/<int:id>/', views.like_question, name='like'),
    path('dislike/<int:id>/', views.dislike_question, name='dislike'),
]