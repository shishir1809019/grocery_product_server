# Generated by Django 4.2.5 on 2023-09-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_in_stock', models.PositiveIntegerField(default=0)),
                ('photo_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
