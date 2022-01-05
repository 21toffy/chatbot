from django.db import models

# Create your models here.


class Question(models.Model):
    stage = models.CharField(max_length=120)
    question_text = models.CharField(max_length=120, null=True, blank=True)
    answer_text = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return f'stage {self.stage}--- {self.question_text}'





class Stages(models.Model):
    stage = models.CharField(max_length=120)
    stage_instruction = models.CharField(max_length=120)

    def __str__(self):
        return f'stage {self.stage}--- {self.stage_instruction}'





class LevelCoordinators(models.Model):
    level = models.CharField(max_length=120, null=True, blank=True)
    coordinator_name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f'stage {self.level}--- {self.coordinator_name}'

