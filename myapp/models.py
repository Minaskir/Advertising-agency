from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    apartment = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.city}, {self.street}, {self.house_number}, {self.apartment}'

class Company(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.company_name

class Contract(models.Model):
    number = models.CharField(max_length=50)
    sign_date = models.DateField()
    expiration_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return self.number

class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создан'),
        ('in_production', 'В производстве'),
        ('completed', 'Завершен'),
    ]
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created')

    def __str__(self):
        return f'Order {self.id}'

class AdProductType(models.Model):
    name = models.CharField(max_length=255)
    graphic_representation = models.ImageField(upload_to='ad_product_types/')

    def __str__(self):
        return self.name

class AdProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    graphic_representation = models.ImageField(upload_to='ad_products/')
    ad_product_type = models.ForeignKey(AdProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=255)
    graphic_representation = models.ImageField(upload_to='templates/')

    def __str__(self):
        return self.name

class WorkAct(models.Model):
    act_number = models.CharField(max_length=50)
    date = models.DateField()
    status = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.act_number

# from django.utils import timezone
# from django.db import models
#
# class Address(models.Model):
#     city = models.CharField(max_length=100, verbose_name='Город')
#     street = models.CharField(max_length=100, verbose_name='Улица')
#     house_number = models.CharField(max_length=10, verbose_name='Номер дома')
#     apartment_number = models.CharField(max_length=10, verbose_name='Номер квартиры', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.city}, {self.street}, {self.house_number}, {self.apartment_number}"
#
# class Company(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Название компании')
#     address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Адрес')
#     phone = models.CharField(max_length=20, verbose_name='Телефон')
#
#     def __str__(self):
#         return self.name
#
# class Manager(models.Model):
#     first_name = models.CharField(max_length=30, verbose_name='Имя')
#     last_name = models.CharField(max_length=30, verbose_name='Фамилия')
#     email = models.EmailField(verbose_name='Электронная почта')
#     phone = models.CharField(max_length=20, verbose_name='Телефон')
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
# class Customer(models.Model):
#     company_name = models.CharField(max_length=100, verbose_name='Название компании')
#     contact_name = models.CharField(max_length=100, verbose_name='Контактное лицо')
#     phone = models.CharField(max_length=20, verbose_name='Телефон')
#     email = models.EmailField(verbose_name='Электронная почта')
#
#     def __str__(self):
#         return self.company_name
#
# class Contract(models.Model):
#     contract_id = models.CharField(max_length=20, verbose_name='Номер договора')
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
#     contract_date = models.DateField(verbose_name='Дата договора', default=timezone.now)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
#
#     def __str__(self):
#         return self.contract_id
#
# class Order(models.Model):
#     order_date = models.DateField(verbose_name='Дата заказа')
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
#     manager = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='Менеджер')
#     contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Договор')
#
#     def __str__(self):
#         return f"Заказ {self.pk} от {self.order_date}"
#
# class AdProductType(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Тип рекламного продукта')
#
#     def __str__(self):
#         return self.name
#
# class AdProduct(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Рекламный продукт')
#     product_type = models.ForeignKey(AdProductType, on_delete=models.CASCADE, verbose_name='Тип продукта')
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#
#     def __str__(self):
#         return self.name
#
# class Template(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Шаблон')
#     file = models.FileField(upload_to='templates/', verbose_name='Файл шаблона')
#
#     def __str__(self):
#         return self.name
#
# class WorkAct(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
#     date = models.DateField(verbose_name='Дата акта')
#     description = models.TextField(verbose_name='Описание работ')
#
#     def __str__(self):
#         return f"Акт {self.pk} для заказа {self.order.pk}"
#
# class WorkAct(models.Model):
#     act_number = models.CharField(max_length=50)
#     date = models.DateField()
#     status = models.CharField(max_length=50)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.act_number

