# Generated by Django 4.2.6 on 2023-11-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newmatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match1Content', models.CharField(max_length=20)),
                ('match2Content', models.CharField(max_length=20)),
                ('match3Content', models.CharField(max_length=20)),
                ('match4Content', models.CharField(max_length=20)),
                ('match5Content', models.CharField(max_length=20)),
                ('match6Content', models.CharField(max_length=20)),
                ('match7Content', models.CharField(max_length=20)),
                ('match8Content', models.CharField(max_length=20)),
                ('match9Content', models.CharField(max_length=20)),
                ('match10Content', models.CharField(max_length=20)),
                ('level1Content', models.CharField(max_length=20)),
                ('level2Content', models.CharField(max_length=20)),
                ('level3Content', models.CharField(max_length=20)),
                ('level4Content', models.CharField(max_length=20)),
                ('level5Content', models.CharField(max_length=20)),
                ('level6Content', models.CharField(max_length=20)),
                ('level7Content', models.CharField(max_length=20)),
                ('level8Content', models.CharField(max_length=20)),
                ('level9Content', models.CharField(max_length=20)),
                ('level10Content', models.CharField(max_length=20)),
            ],
        ),
    ]