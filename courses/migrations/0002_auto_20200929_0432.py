# Generated by Django 3.1 on 2020-09-29 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AddField(
            model_name='coursedate',
            name='currency',
            field=models.CharField(choices=[('HTG', 'HTG')], default='HTG', max_length=25, verbose_name='currency'),
        ),
        migrations.AddField(
            model_name='coursedate',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1000, help_text='Ex: 1000', max_digits=11, max_length=255, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='coursedate',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]