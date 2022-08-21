from django.urls import path

from .views import HomePageView, AboutPageView, TrekCreateView, TrekUpdateView, TrekDetailView, TrekDeleteView, TrekListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('pages/trek-list/', TrekListView.as_view(), name='list_trek'),
    path('<int:pk>/', TrekDetailView.as_view(), name='detail_trek'),
    path('create/', TrekCreateView.as_view(), name='create_trek'),
    path('update/<int:pk>/', TrekUpdateView.as_view(), name='update_trek'),
    path('delete/<int:pk>/', TrekDeleteView.as_view(), name='delete_trek'),
]
