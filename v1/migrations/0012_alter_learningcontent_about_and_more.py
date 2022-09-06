# Generated by Django 4.0.4 on 2022-08-30 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0011_learningcontent_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningcontent',
            name='about',
            field=models.TextField(blank=True, help_text='This field use markdown', null=True, verbose_name='About course'),
        ),
        migrations.AlterField(
            model_name='learningcontent',
            name='experience',
            field=models.TextField(blank=True, help_text='This field use markdown', null=True, verbose_name='What you will learn'),
        ),
        migrations.AlterField(
            model_name='learningcontent',
            name='icon',
            field=models.ImageField(upload_to='v1/images/%Y/%m/', verbose_name='Content icon'),
        ),
        migrations.AlterField(
            model_name='learningcontent',
            name='skills',
            field=models.TextField(blank=True, help_text='This field use markdown', null=True, verbose_name='Skills you will gain'),
        ),
        migrations.AlterField(
            model_name='learningcontent',
            name='underlay',
            field=models.ImageField(upload_to='v1/images/%Y/%m/', verbose_name='Background Image'),
        ),
    ]
