# Generated by Django 4.0.4 on 2022-05-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveBigIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Bad'), (3, '3 - Ok'), (4, '4 - Good'), (5, '5 - Perfect')], null=True),
        ),
    ]
