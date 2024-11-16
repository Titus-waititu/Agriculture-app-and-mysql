from django.shortcuts import redirect, render
from farm.models import Pictures, Post, Testimonials, Blog, Contact, Team

# Create your views here.

def home(request):
    pictures = Pictures.objects.all()
    testimonials = Testimonials.objects.all()
    blogs = Blog.objects.all()
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'pictures': pictures,
        'testimonials': testimonials,
        'blogs': blogs,
        'posts': posts
    })

def about(request):
    teams = Team.objects.all()
    return render(request, 'about.html',{'teams': teams})
   

def blogDetails(request,id):
    posts = Post.objects.get(id=id)
    return render(request, 'blog-details.html',{'posts': posts})

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def testimonials(request):
    testimonials = Testimonials.objects.all()
    return render(request, 'testimonials.html',{'testimonials': testimonials})


def insert_image(request):
    if request.method == 'POST':
        picture = request.FILES['picture']
        message = request.POST['message']
        description = request.POST['description']

        pic = Pictures(
            picture = picture,
            message = message,
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
        return redirect('/contact/')

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

def insert_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        category = request.POST['category']
        content = request.POST['content']
        image = request.FILES['image']
        date = request.POST['date']

        post = Post(
            title = title,
            author = author,
            category = category,
            content = content,
            image = image,
            date = date
        )

        post.save()
        return redirect('/')

    return render(request, 'index.html')

