from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Person

def home_view(request):
    return HttpResponse("Welcome to the home page!")

def about_view(request):
    return HttpResponse("This is the about page")  

def greet_user(request, username):
    return HttpResponse(f"Hello, {username}!")  

def greeting_view(request):
        name_list = request.session.get('name_list', [])
        
        if request.method == 'POST':
            new_name = request.POST.get('name')
            if new_name:
                name_list.append(new_name)
                request.session['name_list'] = name_list

        context = {'names': name_list}
        return render(request, 'greeting.html', context)

def submit_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return render(request, 'submit_result.html', {'name': name})
    return render(request, 'form.html')

def person_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        Person.objects.create(name=name, age=age, comment=comment)
        return redirect('person_list')
    return render(request, 'person_form.html')

def person_list_view(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})

def person_delete_view(request, pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return redirect('person_list')    