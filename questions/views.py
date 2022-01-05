from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer, StagesSerializer
from .models import Question, Stages, LevelCoordinators




def check_for_level(level):
    if "100" in str(level):
        lc = LevelCoordinators.objects.filter(level="100").first()
        return lc.coordinator_name
    elif "200" in str(level):
        lc = LevelCoordinators.objects.filter(level="200").first()
        return lc.coordinator_name
    elif "300" in str(level):
        lc = LevelCoordinators.objects.filter(level="300").first()
        return lc.coordinator_name
    elif "400" in str(level):
        lc = LevelCoordinators.objects.filter(level="400").first()
        return lc.coordinator_name
    elif "500" in str(level):
        lc = LevelCoordinators.objects.filter(level="500").first()
        return lc.coordinator_name
    else :
        return None
    
def check_stage(stage):
    if "1" in str(stage):
        stage_at = Stages.objects.filter(stage = "1").first()
        return stage_at.stage_instruction
    if "2" in str(stage):
        stage_at = Stages.objects.filter(stage = "2").first()
        return stage_at.stage_instruction
    if "3" in str(stage):
        stage_at = Stages.objects.filter(stage = "3").first()
        return stage_at.stage_instruction
    if "4" in str(stage):
        stage_at = Stages.objects.filter(stage = "4").first()
        return stage_at.stage_instruction
    if "5" in str(stage):
        stage_at = Stages.objects.filter(stage = "5").first()
        return stage_at.stage_instruction
    if "6" in str(stage):
        stage_at = Stages.objects.filter(stage = "6").first()
        return stage_at.stage_instruction
    if "7" in str(stage):
        stage_at = Stages.objects.filter(stage = "7").first()
        return stage_at.stage_instruction


class Stage1Views(APIView):


    def get(self, request, stage_id):
        if stage_id == 1:
            query = Question.objects.get(stage = stage_id)
            serializer = QuestionSerializer(query)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        if stage_id == 2:
            query = Question.objects.get(stage = stage_id)
            print(query)
            serializer = QuestionSerializer(query)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"status": "success", "data": "hello world"}, status=status.HTTP_200_OK)



    def post(self, request, stage_id):
        if stage_id == 1:
            # print(request.data["answer_text"])
            request.session['students_name'] = request.data["answer_text"]
            students_name_in_session = request.session["students_name"]
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
 
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                # print(next_stage_question.question_text)
                next_question_completed = "Hello " + students_name_in_session + ", " + next_stage_question.question_text + '.'
                # serializer.save()
                # this would fetch wuestion 2 and return question 2
                return Response({"status": "success", "data": next_question_completed, "stage":"2"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a correct name'
                return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)

        if stage_id == 2:
            # print(request.data["answer_text"])
            student_name = request.session.get("students_name")
            request.session['student_matric'] = request.data["answer_text"]
            students_matric_in_session = request.session["student_matric"]
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
 
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                # print(next_stage_question.question_text)
                next_question_completed = student_name + " " + next_stage_question.question_text + '.'
                # serializer.save()
                # this would fetch wuestion 2 and return question 2
                return Response({"status": "success", "data": next_question_completed, "stage":"3"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a correct name'
                return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)

        if stage_id == 3:
            # print(request.data["answer_text"])
            student_name = request.session.get("students_name")
            student_matric = request.session.get("students_matric")
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
                # print(serializer.data['answer_text'])
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                # check for level

                # print(stinged_next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                # print(next_stage_question.question_text)
                level_inputed_by_user = serializer.data['answer_text']
                level_check = check_for_level(level_inputed_by_user)
                if level_check is None:
                    error_mesage = 'Sorry no level coordinator for this level enter level in this format "100 level, 200 level" '
                    return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    next_question_completed = student_name + f" your level coordinator is  {level_check}" + ", "+ next_stage_question.question_text

                    return Response({"status": "success", "data": next_question_completed, "stage":"4"}, status=status.HTTP_200_OK)
        if stage_id == 4:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                # print(next_stage_question.question_text)
                next_question_completed = next_stage_question.question_text + '.'
                # serializer.save()
                # this would fetch wuestion 2 and return question 2
                return Response({"status": "success", "data": next_question_completed, "stage":"5"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a correct name'
                return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)
        
        if stage_id == 5:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
                have_you_started_reg = serializer.data['answer_text']
                if have_you_started_reg=="yes":
                    next_stage = int(current_stage) + 1
                    stinged_next_stage = str(next_stage)
                    next_stage_question = Question.objects.get(stage = stinged_next_stage)
                    # print(next_stage_question.question_text)
                    next_question_completed = next_stage_question.question_text + '.'
                    # serializer.save()
                    # this would fetch wuestion 2 and return question 2
                    return Response({"status": "success", "data": next_question_completed, "stage":"6"}, status=status.HTTP_200_OK)
                
                elif have_you_started_reg=="no":
                    next_stage = int(current_stage) + 1
                    stinged_next_stage = str(next_stage)
                    next_stage_question = Question.objects.get(stage = stinged_next_stage)
                    # print(next_stage_question.question_text)
                    next_question_completed = next_stage_question.question_text + '.'
                    # serializer.save()
                    # this would fetch wuestion 2 and return question 2
                    return Response({"status": "success", "data": next_question_completed, "stage":"6"}, status=status.HTTP_200_OK)
                    

                else:
                    error_mesage = 'Did not get that, please reply with either yes or no'
                    return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)

        if stage_id == 6:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                stage_number = serializer.data['answer_text']
                current_stage = serializer.data['stage']
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                # print(next_stage_question.question_text)
                next_question_completed = next_stage_question.question_text 
                # serializer.save()
                # this would fetch wuestion 2 and return question 2
                check_stage(stage_number)
                return Response({"status": "success", "data": next_question_completed, "stage":"0"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a stage in this format "stage 1" '
                return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)
