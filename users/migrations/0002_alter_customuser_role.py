# Generated by Django 5.1.7 on 2025-05-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Étudiant')], default='student', max_length=10),
        ),
    ]
