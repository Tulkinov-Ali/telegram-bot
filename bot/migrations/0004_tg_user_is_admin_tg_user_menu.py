# Generated by Django 4.2.5 on 2023-09-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='tg_user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tg_user',
            name='menu',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
