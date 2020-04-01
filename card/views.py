from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Card, Category
from django.views.generic import (
	ListView,
	DetailView
)


def random_card(request: HttpRequest) -> HttpResponse:
	context = {
		'card': Card.objects.order_by('?').first(),
	}
	return render(
		request=request,
		template_name='card/random_card.html',
		context=context)


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


class CategoryListView(ListView):
	model = Category
	template_name = 'card/home.html'

	context_object_name = 'categories'

	ordering = ['name']


class CardListView(ListView):
	"""
	List view with pagination
	"""
	model = Card
	template_name = 'card/cards.html'

	context_object_name = 'cards'
	paginate_by = 12

	def get_queryset(self):
		self.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
		return Card.objects.filter(category=self.category)

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['category'] = self.category
		return context
