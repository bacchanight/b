# Generated by Django 2.2.8 on 2020-03-24 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=125)),
                ('nb_stars', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('detail1', models.BooleanField(default=False)),
                ('detail2', models.BooleanField(default=False)),
                ('detail3', models.BooleanField(default=False)),
                ('detail4', models.BooleanField(default=False)),
                ('detail5', models.BooleanField(default=False)),
                ('id_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Level')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='world',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.World'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('id_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Level')),
            ],
        ),
    ]
