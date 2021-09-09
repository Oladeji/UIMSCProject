# Generated by Django 3.2.3 on 2021-07-03 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0009_auto_20210702_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailresult',
            name='donedate',
            field=models.DateField(default=datetime.datetime(2021, 7, 3, 15, 36, 58, 29317, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='registeredcourse',
            name='dateregistered',
            field=models.DateField(default=datetime.datetime(2021, 7, 3, 15, 36, 58, 27590, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='dateuploaded',
            field=models.DateField(default=datetime.datetime(2021, 7, 3, 15, 36, 58, 25738, tzinfo=utc), verbose_name='Payment Date'),
        ),
    ]