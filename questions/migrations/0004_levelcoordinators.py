# Generated by Django 4.0.1 on 2022-01-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_answer_text_alter_question_question_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelCoordinators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=120, null=True)),
                ('coordinator_name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
