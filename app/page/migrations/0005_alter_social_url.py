# Generated by Django 5.1 on 2024-08-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_social_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
