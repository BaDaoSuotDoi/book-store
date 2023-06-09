# Generated by Django 4.1.7 on 2023-04-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('created_at', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
