# Generated by Django 2.2.8 on 2020-04-07 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('id_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Detail')),
            ],
        ),
    ]
