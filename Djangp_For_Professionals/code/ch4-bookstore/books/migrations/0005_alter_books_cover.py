# Generated by Django 5.1.4 on 2024-12-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]