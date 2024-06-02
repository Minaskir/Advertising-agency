# myapp/forms.py
# from django import forms
# from .models import Address, Company, Manager, Customer, Contract, Order, AdProductType, AdProduct, Template, WorkAct
#
# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = '__all__'
#         labels = {
#             'city': 'Город',
#             'street': 'Улица',
#             'house_number': 'Номер дома',
#             'apartment': 'Квартира',
#         }
#
# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = '__all__'
#
# class ManagerForm(forms.ModelForm):
#     class Meta:
#         model = Manager
#         fields = '__all__'
#
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#
# class ContractForm(forms.ModelForm):
#     class Meta:
#         model = Contract
#         fields = '__all__'
#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#
# class AdProductTypeForm(forms.ModelForm):
#     class Meta:
#         model = AdProductType
#         fields = '__all__'
#         widgets = {
#             'graphic_representation': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
#         }
#
# class AdProductForm(forms.ModelForm):
#     class Meta:
#         model = AdProduct
#         fields = '__all__'
#         widgets = {
#             'graphic_representation': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
#         }
#
# class TemplateForm(forms.ModelForm):
#     class Meta:
#         model = Template
#         fields = '__all__'
#         widgets = {
#             'graphic_representation': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
#         }
#
# class WorkActForm(forms.ModelForm):
#     class Meta:
#         model = WorkAct
#         fields = '__all__'

from django import forms
from .models import Address, Company, Manager, Customer, Contract, Order, AdProductType, AdProduct, Template, WorkAct

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        labels = {
            'city': 'Город',
            'street': 'Улица',
            'house_number': 'Номер дома',
            'apartment': 'Квартира',
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'name': 'Название',
            'contact_info': 'Контактная информация',
        }

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'contact_info': 'Контактная информация',
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'company_name': 'Название компании',
            'contact_name': 'Имя контактного лица',
            'phone': 'Телефон',
            'email': 'Email',
        }

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        labels = {
            'number': 'Номер договора',
            'sign_date': 'Дата подписания',
            'expiration_date': 'Дата окончания',
            'cost': 'Стоимость',
            'payment_status': 'Статус оплаты',
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'contract': 'Договор',
            'manager': 'Менеджер',
            'customer': 'Клиент',
            'quantity': 'Количество',
            'order_date': 'Дата заказа',
            'status': 'Статус',
        }

class AdProductTypeForm(forms.ModelForm):
    class Meta:
        model = AdProductType
        fields = '__all__'
        labels = {
            'name': 'Название',
            'graphic_representation': 'Графическое представление',
        }
        widgets = {
            'graphic_representation': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class AdProductForm(forms.ModelForm):
    class Meta:
        model = AdProduct
        fields = '__all__'
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'graphic_representation': 'Графическое представление',
            'ad_product_type': 'Тип рекламного продукта',
        }
        widgets = {
            'graphic_representation': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = '__all__'
        labels = {
            'name': 'Название',
            'graphic_representation': 'Графическое представление',
        }
        widgets = {
            'graphic_representation': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class WorkActForm(forms.ModelForm):
    class Meta:
        model = WorkAct
        fields = '__all__'
        labels = {
            'act_number': 'Номер акта',
            'date': 'Дата',
            'status': 'Статус',
            'order': 'Заказ',
        }
