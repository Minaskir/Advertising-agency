from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *

def home(request):
    return render(request, 'home.html')

def orders_in_production(request):
    orders = Order.objects.filter(order_date__lte=timezone.now())
    return render(request, 'orders_in_production.html', {'orders': orders})

def customer_orders(request):
    customer_id = request.GET.get('customer_id')
    if customer_id:
        orders = Order.objects.filter(customer_id=customer_id)
    else:
        orders = Order.objects.all()
    return render(request, 'customer_orders.html', {'orders': orders})

def contract_summary(request):
    contracts = Contract.objects.all()
    return render(request, 'contract_summary.html', {'contracts': contracts})

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddressForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Адрес'})

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CompanyForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Компанию'})

def add_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ManagerForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Менеджера'})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Клиента'})

def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContractForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Договор'})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Заказ'})

def add_ad_product_type(request):
    if request.method == 'POST':
        form = AdProductTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdProductTypeForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Тип Рекламного Продукта'})

def add_ad_product(request):
    if request.method == 'POST':
        form = AdProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdProductForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Рекламный Продукт'})

def add_template(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TemplateForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Шаблон'})

def add_work_act(request):
    if request.method == 'POST':
        form = WorkActForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WorkActForm()
    return render(request, 'add_form.html', {'form': form, 'title': 'Добавить Акт Выполненных Работ'})
