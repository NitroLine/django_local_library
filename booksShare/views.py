from django.shortcuts import render
from django.views.generic import View
from .models import Book
from .form import BookForm
from django.shortcuts import redirect
from django.urls import reverse
from  django.db.models import Q
# Create your views here.
def mainlist(request):
    return render(request,'booksShare/index.html')

def books_list(request):
    search=request.GET.get('search','')
    if search:
        AllBooks=Book.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))
    else:
        AllBooks=Book.objects.all()
    AllBooks = AllBooks.filter(count__gte=1)
    return render(request,'booksShare/ListBooks.html',context={'books':AllBooks})

def view_map(request):
    return render(request, 'booksShare/map.html')
def view_about(request):
    return render(request, 'booksShare/about.html')
class BookCreate(View):
    def get(self,request):
        form=BookForm()
        return render(request,'booksShare/NewBook.html',context={'form':form})
    def post(self,request):
        bound_form =BookForm(request.POST,request.FILES)
        if bound_form.is_valid():
            new_book=bound_form.save()
            return redirect('./')
        return render(request,'booksShare/TakeBook.html',context={'form':bound_form})

class BookTake(View):
    def get(self,request):
        search = request.GET.get('search', '')
        if search:
            AllBooks = Book.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))
        else:
            AllBooks = Book.objects.all()
        book=AllBooks.filter(count__gte=1)
        return render(request,'booksShare/TakeBook.html',context={'books':book})
    def post(self,request,id):
        book=Book.objects.get(id=id)
        book.count-=1
        book.save()
        return redirect(reverse('take_book_url'))
        #return render(request,'booksShare/NewBook.html',context={'form':bound_form})

class BookBack(View):
    def get(self,request):
        search = request.GET.get('search', '')
        if search:
            AllBooks = Book.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))
        else:
            AllBooks = Book.objects.all()
        book=AllBooks.filter(count__gte=-1)
        return render(request,'booksShare/BackBook.html',context={'books':book})
    def post(self,request,id):
        book=Book.objects.get(id=id)
        book.count+=1
        book.save()
        return redirect(reverse('back_book_url'))
        #return render(request,'booksShare/NewBook.html',context={'form':bound_form})