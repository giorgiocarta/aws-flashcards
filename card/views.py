from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Card
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request: HttpRequest) -> HttpResponse:
	context = {'title': 'home'}
	return render(
		request=request,
		template_name='card/home.html',
		context=context
	)

def about(request: HttpRequest) -> HttpResponse:
	context = {'title': 'about'}
	return render(
		request=request,
		template_name='card/about.html',
		context=context
	)



class CardDetailView(DetailView):
	model = Card
	fields = ['title', 'content']


class CardListView(ListView):
	"""
	List view with pagination
	"""
	model = Card
	template_name = 'card/cards.html'  # <app> / <model>_<viewtype>.html

	context_object_name = 'cards'
	paginate_by = 12

	def get_queryset(self):
		category = self.kwargs.get('category')
		return Card.objects.filter(category=category.lower())


def topic(request: HttpRequest) -> HttpResponse:
	context = {'title': 'topic'}
	return render(
		request=request,
		template_name='card/topic.html',
		context=context
	)
