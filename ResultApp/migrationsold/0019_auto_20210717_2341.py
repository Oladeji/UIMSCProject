# Generated by Django 3.2.3 on 2021-07-17 23:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0018_auto_20210713_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailresult',
            name='donedate',
            field=models.DateField(default=datetime.datetime(2021, 7, 17, 23, 41, 30, 490637, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='registeredcourse',
            name='dateregistered',
            field=models.DateField(default=datetime.datetime(2021, 7, 17, 23, 41, 30, 488938, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='dateuploaded',
            field=models.DateField(default=datetime.datetime(2021, 7, 17, 23, 41, 30, 487136, tzinfo=utc), verbose_name='Payment Date'),
        ),
    ]
