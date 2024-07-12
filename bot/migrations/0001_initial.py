# Generated by Django 4.2.5 on 2023-09-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tg_user',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, null=True)),
                ('surname', models.CharField(max_length=128, null=True)),
                ('username', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('lang', models.CharField(default='en', max_length=2)),
                ('log', models.JSONField(default={'state': 0})),
            ],
        ),
    ]
