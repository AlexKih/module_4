# Generated by Django 4.2.3 on 2023-07-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisement_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='отметьте, если торг уместен', verbose_name='торг'),
        ),
    ]