# Generated by Django 2.1.1 on 2018-10-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20181003_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='nav',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='导航栏排序'),
        ),
    ]