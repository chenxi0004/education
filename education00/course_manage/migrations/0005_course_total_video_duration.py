# Generated by Django 5.1.5 on 2025-03-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_manage', '0004_learningrecord_video_id_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='total_video_duration',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='课程视频总时长（分钟）'),
        ),
    ]
