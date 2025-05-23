# Generated by Django 5.1.5 on 2025-03-16 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_manage', '0002_learningrecord_learningprogress'),
        ('course_material', '0003_material_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningrecord',
            name='material_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_material.material', verbose_name='学习资料编号'),
        ),
    ]
