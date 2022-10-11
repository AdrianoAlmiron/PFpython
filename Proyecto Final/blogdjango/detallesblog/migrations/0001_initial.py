# Generated by Django 4.1.1 on 2022-10-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detallesblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.CharField(default='DEFAULT VALUE', max_length=60000)),
                ('logo', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_up', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Detallesblog',
            },
        ),
    ]