from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product

def home(request):
    products = Product.objects.all()[:8]
    categories = Category.objects.all()
    return render(request, 'home.html', {  # Просто home.html
        'products': products,
        'categories': categories
    })

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Просто product_list.html
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object)
        return context