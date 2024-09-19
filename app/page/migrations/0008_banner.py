# Generated by Django 5.1 on 2024-08-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_rename_url_social_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='default.png', upload_to='banners')),
                ('title', models.CharField(max_length=100)),
                ('sort', models.IntegerField(default=1)),
            ],
        ),
    ]
