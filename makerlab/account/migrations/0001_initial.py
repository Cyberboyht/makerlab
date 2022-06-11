# Generated by Django 3.1.5 on 2022-06-11 23:11

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='Ex:john@winterfell.got', max_length=255, unique=True, verbose_name='Email ')),
                ('first_name', models.CharField(help_text='Ex:john', max_length=150, verbose_name='Prénom')),
                ('last_name', models.CharField(help_text='Ex:snow', max_length=150, verbose_name='Nom')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Ex:+509XXXXXXXX', max_length=15, region=None, verbose_name='Téléphone')),
                ('country', django_countries.fields.CountryField(blank=True, default='HT', help_text='Selectionner votre pays', max_length=2, verbose_name='Pays')),
                ('photo', models.ImageField(blank=True, default=None, upload_to='account_photos')),
                ('email_verified', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
