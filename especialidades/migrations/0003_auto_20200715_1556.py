# Generated by Django 3.0.8 on 2020-07-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0002_auto_20200713_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especilidade',
            name='id_especialidad',
        ),
        migrations.AlterField(
            model_name='especilidade',
            name='titulo',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]