# Generated by Django 4.1.4 on 2023-01-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]
