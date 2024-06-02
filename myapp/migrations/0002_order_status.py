# Generated by Django 4.2.13 on 2024-05-31 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Создан'), ('in_production', 'В производстве'), ('completed', 'Завершен')], default='created', max_length=50),
        ),
    ]
