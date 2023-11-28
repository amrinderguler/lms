from django.shortcuts import render , get_object_or_404
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    return render(request,"home.html",context={"current_tab":"home"})

def readers(request):
    return render(request,"readers.html",context={"current_tab":"readers"})

def shopping(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    student_name=request.POST['student_name']
    return render(request,"welcome.html",context={'student_name':student_name})

def readers_tab(request):
    query=request.GET.get('q')
    if query:
        readers=reader.objects.filter(reference_id__icontains=query)
    else:
        readers=reader.objects.all()
    return render(request, "readers.html", context={"current_tab":"readers", "readers":readers})

def save_reader(request):
    reader_item=reader(reference_id=request.POST['reader_refrenceID'],
                       reader_name=request.POST['reader_name'],
                       reader_contact=request.POST['reader_contact'],
                       reader_address=request.POST['reader_address'],
                       active=True
                       )
    reader_item.save()
    return redirect('/readers')

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})



def add_to_bag(request, book_id):
    try:
        book = get_object_or_404(Book, id=book_id)
        bag = Bag.objects.create(book=book, quantity=1)
        return redirect('/books')
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")

def my_bag(request):
    # Get all Bag objects
    bags = Bag.objects.all()

    # Pass the bags to the template
    return render(request, 'my_bag.html', {'bags': bags})

def remove_from_bag(request, book_id):
    try:
        # Get the book to be removed
        book = get_object_or_404(Book, id=book_id)
        
        # Get the bag item
        bag_item = get_object_or_404(Bag, book=book)
        
        # Remove the book from the bag
        bag_item.delete()
        
        return redirect('/mybag')
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")