# Generated by Django 2.2 on 2020-03-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0006_auto_20200321_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='desc',
            field=models.TextField(default='write here', null=True),
        ),
    ]