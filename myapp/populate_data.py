# myapp/populate_data.py

import datetime
from django.utils import timezone
from myapp.models import Address, Company, Manager, Customer, Contract, Order, AdProductType, AdProduct, Template, WorkAct

def populate():
    # Создание адресов
    address1 = Address.objects.create(city='Москва', street='Ленина', house_number='10', apartment='5')
    address2 = Address.objects.create(city='Санкт-Петербург', street='Невский', house_number='20', apartment='10')

    # Создание компаний
    company1 = Company.objects.create(name='Компания А', contact_info='Контактная информация компании А')
    company2 = Company.objects.create(name='Компания Б', contact_info='Контактная информация компании Б')

    # Создание менеджеров
    manager1 = Manager.objects.create(name='Менеджер 1', contact_info='Контактная информация менеджера 1')
    manager2 = Manager.objects.create(name='Менеджер 2', contact_info='Контактная информация менеджера 2')

    # Создание клиентов
    customer1 = Customer.objects.create(company_name='Клиент 1', contact_name='Контактное лицо 1', phone='1234567890', email='client1@example.com')
    customer2 = Customer.objects.create(company_name='Клиент 2', contact_name='Контактное лицо 2', phone='0987654321', email='client2@example.com')

    # Создание типов рекламных продуктов
    ad_product_type1 = AdProductType.objects.create(name='Баннер', graphic_representation='URL к графическому представлению баннера')
    ad_product_type2 = AdProductType.objects.create(name='Биллборд', graphic_representation='URL к графическому представлению биллборда')

    # Создание рекламных продуктов
    ad_product1 = AdProduct.objects.create(name='Баннер 1', description='Описание баннера 1', graphic_representation='URL к графическому представлению баннера 1', ad_product_type=ad_product_type1)
    ad_product2 = AdProduct.objects.create(name='Биллборд 1', description='Описание биллборда 1', graphic_representation='URL к графическому представлению биллборда 1', ad_product_type=ad_product_type2)

    # Создание шаблонов
    template1 = Template.objects.create(name='Шаблон 1', graphic_representation='URL к графическому представлению шаблона 1')
    template2 = Template.objects.create(name='Шаблон 2', graphic_representation='URL к графическому представлению шаблона 2')

    # Создание договоров
    contract1 = Contract.objects.create(number='Договор 1', sign_date=timezone.now(), expiration_date=timezone.now() + datetime.timedelta(days=365), cost=1000.00, payment_status='Оплачено')
    contract2 = Contract.objects.create(number='Договор 2', sign_date=timezone.now(), expiration_date=timezone.now() + datetime.timedelta(days=365), cost=2000.00, payment_status='Не оплачено')

    # Создание заказов
    order1 = Order.objects.create(contract=contract1, manager=manager1, customer=customer1, quantity=10, order_date=timezone.now())
    order2 = Order.objects.create(contract=contract2, manager=manager2, customer=customer2, quantity=20, order_date=timezone.now())

    # Создание актов выполненных работ
    work_act1 = WorkAct.objects.create(act_number='Акт 1', date=timezone.now(), status='Завершено', order=order1)
    work_act2 = WorkAct.objects.create(act_number='Акт 2', date=timezone.now(), status='В процессе', order=order2)

    print("Данные успешно заполнены!")
