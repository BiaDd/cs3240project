# Generated by Django 3.2.7 on 2021-10-29 23:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0002_auto_20211023_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='class', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 23, 18, 18, 887350, tzinfo=utc), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 23, 18, 18, 887375, tzinfo=utc), verbose_name='due date'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(default=datetime.datetime(2021, 10, 29, 23, 18, 18, 887986, tzinfo=utc), verbose_name='date joined')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
