# Generated by Django 4.0.4 on 2022-07-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_roomscost_cost_el_roomsdevices_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.AlterModelOptions(
            name='roomsaccessories',
            options={'verbose_name': 'Аксессуар', 'verbose_name_plural': 'Аксессуары'},
        ),
        migrations.AlterModelOptions(
            name='roomsdevices',
            options={'verbose_name': 'Девайс', 'verbose_name_plural': 'Девайсы'},
        ),
    ]