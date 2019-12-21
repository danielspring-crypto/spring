from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
	context = {
		'posts':Post.objects.order_by("-date_posted")
	}
	return render(request, "gallery/index.html", context)