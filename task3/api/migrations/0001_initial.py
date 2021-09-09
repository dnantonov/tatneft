# Generated by Django 3.2.7 on 2021-09-09 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('currency', models.CharField(choices=[('rub', 'rub'), ('euro', 'euro'), ('dol', 'dol')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.image')),
            ],
        ),
        migrations.CreateModel(
            name='SecondGasStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fuel')),
            ],
        ),
        migrations.AddField(
            model_name='fuel',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.image'),
        ),
        migrations.CreateModel(
            name='FirstGasStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coordinates', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
            ],
        ),
    ]