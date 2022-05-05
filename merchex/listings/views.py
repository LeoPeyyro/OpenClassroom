from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def band_list(request):
	bands = Band.objects.all()
	return render(request,
		'listings/band_list.html',
		{'bands': bands})

def about(request):
	return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')

def band_detail(request, id):
	band = Band.objects.get(id=id)
	return render(request,
		'listings/band_detail.html',
		{'band': band})