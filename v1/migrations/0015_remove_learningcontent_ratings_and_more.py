# Generated by Django 4.0.4 on 2022-08-30 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0014_remove_rating_course_learningcontent_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningcontent',
            name='ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='learning_content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='v1.learningcontent'),
            preserve_default=False,
        ),
    ]