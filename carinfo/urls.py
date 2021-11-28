from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),
    path('maker/<str:carmaker>', views.ModelListView.as_view(),name="carmaker"),
    path('search-result', views.SearchResultView.as_view(),name="search")
]
