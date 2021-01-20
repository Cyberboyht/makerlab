# Generated by Django 3.0.8 on 2021-01-20 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False, verbose_name='complete')),
                ('score', models.DecimalField(decimal_places=2, default=0, help_text='Ex: 18.5', max_digits=11, max_length=255, verbose_name='score')),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='attendee')),
            ],
            options={
                'verbose_name_plural': 'Attendees',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Ex: c++ Introduction', max_length=255, verbose_name='title')),
                ('links', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.URLField(), blank=True, help_text='Ex: https://www.site.com/something.pdf', null=True, size=None, verbose_name='please add link')),
                ('note', models.TextField(blank=True, help_text='some additional note', null=True, verbose_name='note')),
                ('description', models.TextField(help_text='some description', verbose_name='description')),
                ('tags', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(), blank=True, help_text='Ex: Arduino', null=True, size=None, verbose_name='please add tag')),
                ('photo', models.ImageField(blank=True, default=None, upload_to='courses_photos')),
                ('requirements', models.ManyToManyField(blank=True, to='courses.Course', verbose_name='requirements')),
            ],
            options={
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='CourseDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=1000, help_text='Ex: 1000', max_digits=11, max_length=255, verbose_name='price')),
                ('currency', models.CharField(choices=[('HTG', 'HTG')], default='HTG', max_length=25, verbose_name='currency')),
                ('date', models.DateTimeField(max_length=255, verbose_name='date')),
                ('nb_attendees', models.IntegerField(help_text='Ex: 50', verbose_name='number of attendees')),
                ('attendees', models.ManyToManyField(blank=True, related_name='attendees', through='courses.Attendee', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseDates', to='courses.Course', verbose_name='course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Course Dates',
                'get_latest_by': 'date',
            },
        ),
        migrations.AddField(
            model_name='attendee',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseDate', verbose_name='date'),
        ),
    ]
