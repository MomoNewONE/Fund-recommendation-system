# Generated by Django 4.2.6 on 2023-12-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.CharField(default='default_value', max_length=100)),
                ('x2', models.CharField(default='default_value', max_length=100)),
                ('x3', models.CharField(default='default_value', max_length=100)),
                ('x4', models.CharField(default='default_value', max_length=100)),
                ('x5', models.CharField(default='default_value', max_length=100)),
                ('x6', models.CharField(default='default_value', max_length=100)),
                ('x7', models.CharField(default='default_value', max_length=100)),
                ('x8', models.CharField(default='default_value', max_length=100)),
                ('x9', models.CharField(default='default_value', max_length=100)),
                ('x10', models.CharField(default='default_value', max_length=100)),
                ('x11', models.CharField(default='default_value', max_length=100)),
                ('x12', models.CharField(default='default_value', max_length=100)),
                ('x13', models.CharField(default='default_value', max_length=100)),
                ('x14', models.CharField(default='default_value', max_length=100)),
                ('x15', models.CharField(default='default_value', max_length=100)),
                ('x16', models.CharField(default='default_value', max_length=100)),
                ('x17', models.CharField(default='default_value', max_length=100)),
                ('x18', models.CharField(default='default_value', max_length=100)),
                ('x19', models.CharField(default='default_value', max_length=100)),
            ],
        ),
    ]