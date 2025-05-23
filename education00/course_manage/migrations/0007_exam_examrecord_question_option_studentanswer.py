# Generated by Django 5.1.5 on 2025-04-05 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_manage', '0006_learningrecord_is_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.AutoField(primary_key=True, serialize=False, verbose_name='考试编号')),
                ('exam_name', models.CharField(max_length=100, verbose_name='考试名称')),
                ('exam_description', models.TextField(verbose_name='考试描述')),
                ('start_time', models.DateTimeField(verbose_name='考试开始时间')),
                ('end_time', models.DateTimeField(verbose_name='考试结束时间')),
                ('duration', models.IntegerField(verbose_name='考试时长（分钟）')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_manage.course', verbose_name='课程编号')),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='ExamRecord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False, verbose_name='考试记录编号')),
                ('student_id', models.CharField(max_length=20, verbose_name='学生编号')),
                ('score', models.FloatField(blank=True, null=True, verbose_name='考试成绩')),
                ('exam_time', models.DateTimeField(auto_now_add=True, verbose_name='考试时间')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_manage.exam', verbose_name='考试编号')),
            ],
            options={
                'db_table': 'exam_record',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False, verbose_name='题目编号')),
                ('question_type', models.CharField(choices=[('single_choice', '单选题'), ('multiple_choice', '多选题'), ('true_false', '判断题'), ('fill_in_the_blank', '填空题'), ('essay', '综合题')], max_length=20, verbose_name='题目类型')),
                ('question_text', models.TextField(verbose_name='题目内容')),
                ('answer', models.TextField(verbose_name='答案')),
                ('score', models.FloatField(verbose_name='分值')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_manage.exam', verbose_name='考试编号')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False, verbose_name='选项编号')),
                ('option_text', models.CharField(max_length=255, verbose_name='选项内容')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_manage.question', verbose_name='题目编号')),
            ],
            options={
                'db_table': 'option',
            },
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='答题记录编号')),
                ('student_answer', models.TextField(verbose_name='学生答案')),
                ('is_correct', models.BooleanField(blank=True, null=True, verbose_name='是否正确')),
                ('exam_record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_manage.examrecord', verbose_name='考试记录编号')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_manage.question', verbose_name='题目编号')),
            ],
            options={
                'db_table': 'student_answer',
            },
        ),
    ]
