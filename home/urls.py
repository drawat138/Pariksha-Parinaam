from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('jobs/',views.jobs),
    path('detail/<id>',views.detail),
    path('result/',views.result),
    path('admitcard',views.admitcard),
    path('answerkey',views.answerkey),
]