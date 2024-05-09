# Generated by Django 5.0.4 on 2024-05-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_orderplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='team')),
            ],
        ),
    ]