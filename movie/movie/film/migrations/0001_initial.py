# Generated by Django 4.2.2 on 2023-06-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='book/img')),
            ],
        ),
    ]
