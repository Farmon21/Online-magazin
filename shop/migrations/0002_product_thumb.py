# Generated by Django 4.0.4 on 2022-04-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(default='default_product.jpg', upload_to=''),
        ),
    ]