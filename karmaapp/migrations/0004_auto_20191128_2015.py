# Generated by Django 2.2.4 on 2019-11-29 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karmaapp', '0003_auto_20191128_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aglutinado',
            name='tipo_ajuste',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='block',
            name='tipo_ajuste',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cilindro',
            name='tipo_ajuste',
            field=models.CharField(max_length=200),
        ),
    ]
