# Generated by Django 3.2.3 on 2021-07-08 10:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0013_auto_20210705_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='emailaddress',
        ),
        migrations.RemoveField(
            model_name='biodata',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='student',
            name='emailaddress',
            field=models.EmailField(default='MscDefault@ui.ng', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='phonenumber',
            field=models.CharField(default='234', max_length=40),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='fieldofinterest',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='detailresult',
            name='donedate',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 10, 38, 5, 941732, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='registeredcourse',
            name='dateregistered',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 10, 38, 5, 940010, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='dateuploaded',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 10, 38, 5, 938179, tzinfo=utc), verbose_name='Payment Date'),
        ),
    ]
