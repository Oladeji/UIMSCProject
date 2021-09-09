# Generated by Django 3.2.3 on 2021-06-26 22:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0006_auto_20210626_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='semester',
            new_name='asemester',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='asetid',
            new_name='aset',
        ),
        migrations.AlterField(
            model_name='detailresult',
            name='donedate',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 22, 2, 11, 487443, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='registeredcourse',
            name='dateregistered',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 22, 2, 11, 485747, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='dateuploaded',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 22, 2, 11, 483865, tzinfo=utc), verbose_name='Payment Date'),
        ),
    ]
