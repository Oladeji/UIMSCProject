# Generated by Django 3.2.3 on 2021-06-04 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ResultApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asemester',
            old_name='aset',
            new_name='asession',
        ),
        migrations.AlterField(
            model_name='detailresult',
            name='donedate',
            field=models.DateField(default=datetime.datetime(2021, 6, 4, 15, 36, 16, 361360, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='registeredcourse',
            name='dateregistered',
            field=models.DateField(default=datetime.datetime(2021, 6, 4, 15, 36, 16, 359711, tzinfo=utc), verbose_name='Registered Date'),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='dateuploaded',
            field=models.DateField(default=datetime.datetime(2021, 6, 4, 15, 36, 16, 357993, tzinfo=utc), verbose_name='Payment Date'),
        ),
    ]
