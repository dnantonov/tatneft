# Generated by Django 3.2.7 on 2021-09-09 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210909_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='GasStation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coordinates', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fuel')),
                ('images', models.ManyToManyField(blank=True, null=True, to='api.Image')),
                ('services', models.ManyToManyField(blank=True, null=True, to='api.Service')),
            ],
        ),
        migrations.RemoveField(
            model_name='secondgasstation',
            name='fuel',
        ),
        migrations.DeleteModel(
            name='FirstGasStation',
        ),
        migrations.DeleteModel(
            name='SecondGasStation',
        ),
    ]
