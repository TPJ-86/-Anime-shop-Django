from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']



class Supplier(models.Model):
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150, blank=True)
    address = models.TextField(blank=True)

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'



class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']


class Customer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    class Meta:
        db_table = 'customer'
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'



class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'




class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    products = models.ManyToManyField(Product, through='OrderItem')

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date']



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'

