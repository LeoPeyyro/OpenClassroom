from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ListingForm, BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

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

def band_create(request):
	if request.method == 'POST':
		form = BandForm(request.POST)
		if form.is_valid():
			band = form.save()
			return redirect('band-detail', band.id)
	else:
		form = BandForm()
	return render(request,
		'listings/band_create.html',
		{'form': form})

def listing_list(request):
	listings = Listing.objects.all()
	return render(request,
		'listings/listing_list.html',
		{'listings': listings})

def listing_detail(request, id):
	listing = Listing.objects.get(id=id)
	return render(request,
		'listings/listing_detail.html',
		{'listing': listing})

def listing_create(request):
	if request.method == 'POST':
		form = ListingForm(request.POST)
		if form.is_valid():
			listing = form.save()
			return redirect('listing-detail', listing.id)
	else:
		form = ListingForm()
	return render(request,
		'listings/listing_create.html',
		{'form': form})

def contact(request):
	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid():
				send_mail(
				subject=f'Message de {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
				message=form.cleaned_data['message'],
				from_email=form.cleaned_data['email'],
				recipient_list=['leo.perreaut@laposte.net']
			)
		return redirect('email-sent')
	else:
		form = ContactUsForm()
	return render(request,
		'listings/contact.html',
		{'form': form}) 

def email_sent(request):
	return render(request,
		'listings/email_sent.html')