# Generated by Django 3.0.8 on 2020-07-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especilidade',
            fields=[
                ('id_especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('cantidad_profesionales', models.IntegerField()),
                ('cantidad_citas', models.IntegerField()),
            ],
        ),
    ]