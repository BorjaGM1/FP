# Generated by Django 4.0 on 2022-01-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imgurl',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
