# Generated by Django 5.0.4 on 2024-05-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AlterField(
            model_name='emp',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
