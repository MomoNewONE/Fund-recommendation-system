# Generated by Django 4.2.6 on 2023-11-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_newrank_delete_ranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code1Content', models.CharField(max_length=20)),
                ('code2Content', models.CharField(max_length=20)),
                ('code3Content', models.CharField(max_length=20)),
                ('code4Content', models.CharField(max_length=20)),
                ('code5Content', models.CharField(max_length=20)),
                ('code6Content', models.CharField(max_length=20)),
                ('code7Content', models.CharField(max_length=20)),
                ('code8Content', models.CharField(max_length=20)),
                ('code9Content', models.CharField(max_length=20)),
                ('code10Content', models.CharField(max_length=20)),
            ],
        ),
    ]
