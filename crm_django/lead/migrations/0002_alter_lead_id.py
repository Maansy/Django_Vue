# Generated by Django 4.2.3 on 2023-07-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]