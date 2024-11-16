from django.shortcuts import redirect, render
from farm.models import Pictures, Testimonials, Blog, Contact, Team

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
        picture = request.FILES['picture']
        description = request.POST['description']

        pic = Pictures(
            picture = picture,
            description = description
        )

        pic.save()
        return redirect('/')

    return render(request, 'index.html')

def insert_testimonial(request):
    if request.method == 'POST':
        picture = request.FILES['picture']
        message = request.POST['message']
        name = request.POST['name']

        testimonial = Testimonials(
            picture = picture,
            message = message,
            name = name
        )

        testimonial.save()
        return redirect('/')

    return render(request, 'index.html')

def insert_blog(request):
    if request.method == 'POST':
        date = request.POST['date']
        picture = request.FILES['picture']
        name = request.POST['name']
        description = request.POST['description']

        blog = Blog(
            date = date,
            picture = picture,
            name = name,
            description = description
        )

        blog.save()
        return redirect('/')

    return render(request, 'index.html')

def insert_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(
            name = name,
            email = email,
            subject = subject,
            message = message
        )

        contact.save()
        return redirect('/')

    return render(request, 'index.html')

def insert_team(request):
    if request.method == 'POST':
        picture = request.FILES['picture']
        name = request.POST['name']
        designation = request.POST['designation']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']

        team = Team(
            picture = picture,
            name = name,
            designation = designation,
            facebook = facebook,
            twitter = twitter,
            linkedin = linkedin
        )

        team.save()
        return redirect('/')

    return render(request, 'index.html')

def admin_page(request):
    return render(request, 'admin_page.html')