from django.urls import path
from . import views

urlpatterns = [
	path('', views.CategoryListView.as_view(), name='cards-home'),
	path('about/', views.about, name='cards-about'),
	path('card/<str:category>/<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
	path('cards/<int:pk>', views.CardListView.as_view(), name='cards')
]
