# Generated by Django 3.2.6 on 2021-09-06 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, unique=True)),
                ('author_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='book_cover/')),
                ('added_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('slug', models.SlugField(max_length=250)),
                ('quantity', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='shop.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
