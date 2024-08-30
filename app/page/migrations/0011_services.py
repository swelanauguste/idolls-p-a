# Generated by Django 5.1 on 2024-08-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_alter_value_desc_alter_whyus_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, default='default.png', null=True, upload_to='values')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(verbose_name='Description')),
                ('sort', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['sort'],
            },
        ),
    ]
