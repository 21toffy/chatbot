# Generated by Django 4.0.1 on 2022-01-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_stages'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]