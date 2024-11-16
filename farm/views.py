from django.shortcuts import redirect, render
from farm.models import Pictures

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blogDetails(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def testimonials(request):
    return render(request, 'testimonials.html')


def insert_image(request):
    if request.method == 'POST':
        picture = request.POST['picture']
        description = request.POST['description']

        pic = Pictures(
            picture = picture,
            description = description
        )

        pic.save()
        return redirect('/')
