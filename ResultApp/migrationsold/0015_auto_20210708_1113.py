# Generated by Django 3.2.3 on 2021-07-08 11:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0014_auto_20210708_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='000', max_length=50),
        ),
        migrations.AlterField(
            model_name='detailresult',
            name='donedate',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 11, 13, 12, 346106, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='registeredcourse',
            name='dateregistered',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 11, 13, 12, 344411, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='dateuploaded',
            field=models.DateField(default=datetime.datetime(2021, 7, 8, 11, 13, 12, 342537, tzinfo=utc), verbose_name='Payment Date'),
        ),
    ]
