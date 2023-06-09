# Generated by Django 3.0.5 on 2020-04-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('pid', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=255)),
                ('status', models.SmallIntegerField(default=1)),
                ('addtime', models.FloatField(default=0.0, max_length=30)),
            ],
        ),
    ]
