# Generated by Django 5.0.4 on 2024-05-07 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
