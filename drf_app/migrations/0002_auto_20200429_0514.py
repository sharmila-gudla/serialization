# Generated by Django 3.0 on 2020-04-29 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drf_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drf_app.User'),
        ),
    ]
