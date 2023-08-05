# Generated by Django 4.2.2 on 2023-08-04 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('user_img', models.ImageField(blank=True, null=True, upload_to='user_image/')),
                ('id_sex', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('idaddress', models.IntegerField(primary_key=True, serialize=False)),
                ('postalcode', models.IntegerField()),
                ('cityname', models.CharField(max_length=100)),
                ('addresslineone', models.CharField(max_length=100)),
                ('addresslinetwo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('idrole', models.IntegerField(primary_key=True, serialize=False)),
                ('rolename', models.CharField(max_length=100, unique=True)),
                ('rolepermission', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]