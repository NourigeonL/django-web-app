from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
  <h1>Hello Django !</h1>
  <p>My favorite groups are :<p>
  <ul>
    <li>{bands[0].name}</li>
    <li>{bands[1].name}</li>
    <li>{bands[2].name}</li>
  </ul>
  """)


def about(request):
    return HttpResponse('<h1>About us</h1> <p>We love merch !</p>')


def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
    <h1>Listings</h1> 
    <p>The list of the ads:</p>
    <ul>
      <li>{listings[0].title}</li>
      <li>{listings[1].title}</li>
      <li>{listings[2].title}</li>
      <li>{listings[3].title}</li>
    </ul>
    """)


def contact(request):
    return HttpResponse("<h1>Contact us</h1> <p>Oupsy you can't contact us lol</p>")
