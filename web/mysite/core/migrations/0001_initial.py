# Generated by Django 2.1.3 on 2020-09-15 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='clothings/images/')),
            ],
        ),
        migrations.CreateModel(
            name='CoordinateClothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_kind', models.IntegerField()),
                ('c_image', models.ImageField(blank=True, upload_to='')),
                ('c_url', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]