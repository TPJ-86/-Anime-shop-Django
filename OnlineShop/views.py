from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    """Главная страница"""
    products = Product.objects.all()[:8]
    categories = Category.objects.all()[:6]
    return render(request, 'home.html', {
        'products': products,
        'categories': categories
    })

def products(request):
    """Все товары"""
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})

def product_detail(request, id):
    """Детали товара"""
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def category_list(request):
    """Список категорий"""
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, id):
    """Товары в категории"""
    category = get_object_or_404(Category, id=id)
    products_in_category = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {
        'category': category,
        'products': products_in_category
    })