# Generated by Django 3.2.7 on 2021-11-06 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_document_docfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='course',
        ),
        migrations.AddField(
            model_name='document',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
