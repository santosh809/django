# Generated by Django 4.0.6 on 2022-08-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='media')),
                ('icon', models.CharField(max_length=40)),
                ('remark', models.TextField()),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
    ]
