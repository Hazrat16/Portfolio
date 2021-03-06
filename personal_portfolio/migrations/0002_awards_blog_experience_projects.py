# Generated by Django 3.1 on 2020-10-30 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.IntegerField()),
                ('nameOfAwards', models.CharField(max_length=100)),
                ('awardFrom', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromYear', models.IntegerField()),
                ('toYear', models.IntegerField()),
                ('nameOfPost', models.CharField(max_length=100)),
                ('nameOfCompany', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectTitle', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('projectType', models.CharField(max_length=200)),
            ],
        ),
    ]
