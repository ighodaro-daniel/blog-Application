
from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
    path('',views.index,name='home'),
    path("<int:question_id>/",views.detail,name='detail'),
    path("<int:question_id>/result",views.result,name='result'),
    path("<int:question_id>/deleteText",views.deleteText,name="deleteText"),
    path("create/",views.createText,name='create')
]