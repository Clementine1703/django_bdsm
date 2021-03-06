# Generated by Django 4.0.4 on 2022-07-10 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_site_alter_roomsaccessories_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'verbose_name': 'Здесь ты можешь добавлять/удалять новые правила и изменять контакты!', 'verbose_name_plural': 'Настройки сайта'},
        ),
        migrations.CreateModel(
            name='SiteRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(max_length=200, verbose_name='правило')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.site')),
            ],
        ),
        migrations.CreateModel(
            name='SiteContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, verbose_name='номер телефона')),
                ('email', models.CharField(max_length=200, verbose_name='email')),
                ('address', models.CharField(max_length=500, verbose_name='адрес')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.site')),
            ],
        ),
    ]
