from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy 


from django.core.files.storage import FileSystemStorage

from .models import Book
from .forms import BookForm

class Home(TemplateView):
	template_name = 'home.html'


def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		print(uploaded_file.name)
		print(uploaded_file.size)
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		context['url'] = fs.url(name)
	return render(request, 'upload.html', context)


def book_list(request):
	books = Book.objects.all()
	context = {'books': books}
	return render(request,'book_list.html', context)


def upload_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('book_list')
	else:
		form = BookForm()
	context = {'form': form}
	return render(request, 'upload_book.html', context)


def delete_book(request,pk):
	if request.method == 'POST':
		book = Book.objects.get(pk=pk)
		book.delete()
	return redirect('book_list')
	

class BookListView(ListView):
	model = Book
	template_name = 'class_book_list.html'
	context_object_name = 'books'


class UploadBookView(CreateView):
	model = Book
	fields = ('title', 'author', 'pdf', 'cover')
	success_url = reverse_lazy('class_book_list')
	template_name = 'upload_book.html'