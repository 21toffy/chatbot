from rest_framework import serializers
from .models import Question, Stages

class QuestionSerializer(serializers.ModelSerializer):
    stage = serializers.CharField(max_length=120)
    question_text = serializers.CharField(max_length=120)
    answer_text = serializers.CharField(max_length=120)


    class Meta:
        model = Question
        fields = ('__all__')



class StagesSerializer(serializers.ModelSerializer):
    stage = serializers.CharField(max_length=120)
    stage_instruction = serializers.CharField(max_length=120)

    class Meta:
        model = Stages
        fields = ('__all__')