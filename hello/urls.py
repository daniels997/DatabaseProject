from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("query1", views.query1, name="query1"),
    path("query2", views.query2, name="query2"),
    path("query3", views.query3, name="query3"),
    path("query4", views.query4, name="query4"),
    path("query5", views.query5, name="query5"),
    path("query6", views.query6, name="query6"),
    path("query7", views.query7, name="query7")
]