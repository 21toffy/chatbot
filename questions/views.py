from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer, StagesSerializer
from .models import Question, Stages, LevelCoordinators




def check_for_level(level, request):
    if "100" in str(level):
        lc = LevelCoordinators.objects.filter(level="100").first()
        request.session['student_level'] = "100"
        return lc.coordinator_name
    elif "200" in str(level):
        lc = LevelCoordinators.objects.filter(level="200").first()
        request.session['student_level'] = "200"
        return lc.coordinator_name
    elif "300" in str(level):
        lc = LevelCoordinators.objects.filter(level="300").first()
        request.session['student_level'] = "300"
        return lc.coordinator_name
    elif "400" in str(level):
        lc = LevelCoordinators.objects.filter(level="400").first()
        request.session['student_level'] = "400"
        return lc.coordinator_name
    elif "500" in str(level):
        lc = LevelCoordinators.objects.filter(level="500").first()
        request.session['student_level'] = "500"
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
            print(serializer.data)
            # new_dict = {
            #     "question_text": serializer.data["question_text"],
            #     "stage":"1",
            #     "next_stage":"2"
            # }
            return Response({"status": "success", "question_text": serializer.data["question_text"],
                "stage":"1",
                "next_stage":"2", "from":"bot"}, status=status.HTTP_200_OK)
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
            students_name_in_session = request.session.get("students_name")
            print(students_name_in_session)
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
 
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                print(stinged_next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                print(next_stage_question)
                next_question_completed = "Hello " + students_name_in_session + ", " + next_stage_question.question_text + '.'
                # serializer.save()
                # this would fetch wuestion 2 and return question 2
                return Response({"status": "success", "question_text": next_question_completed, "stage":"1", "next_stage":"2", "from":"bot"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a correct name'
                return Response({"status": "error", "question_text": error_mesage}, status=status.HTTP_400_BAD_REQUEST)


        # type in matric 
        if stage_id == 2:
            # print(request.data["answer_text"])
            print(request.data)
            request.session['student_matric'] = request.data["answer_text"]
            
            students_name_in_session = request.session.get("students_name")
            # students_name_in_session = request.session["students_name"]
            students_matric_in_session = request.session["student_matric"]

            print(students_name_in_session)
            
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
 
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                print(stinged_next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                print(next_stage_question)
                next_question_completed = "your matric number " + students_matric_in_session + ", " + next_stage_question.question_text + '.'
                # serializer.save()
                # this would fetch wuestion 2 and return question 2
                return Response({"status": "success", "question_text": next_question_completed, "stage":"2", "next_stage":"3", "from":"bot"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a correct name'
                return Response({"status": "error", "question_text": error_mesage}, status=status.HTTP_400_BAD_REQUEST)


        if stage_id == 3:
            
            student_name = request.session.get("students_name")
            request.session['student_level'] = request.data["answer_text"]

            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer.data)
                current_stage = serializer.data['stage']
                # print(serializer.data['answer_text'])
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                # check for level
                # print(stinged_next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                # print(next_stage_question.question_text)
                level_inputed_by_user = serializer.data['answer_text']
                level_check = check_for_level(level_inputed_by_user, request)
                if level_check is None:
                    error_mesage = 'Sorry no level coordinator for this level enter level in this format "100 level, 200 level" '
                    return Response({"status": "error", "question_text": error_mesage, "stage":"2","from": "bot", "next_stage":"3"}, status=status.HTTP_200_OK)
                    

                else:
                    next_question_completed = "Dear student" + f" your level coordinator is  {level_check}" + ", "+ next_stage_question.question_text

                    return Response({"status": "success", "question_text": next_question_completed, "stage":"3", "next_stage":"4", "from":"bot"}, status=status.HTTP_200_OK)

        if stage_id == 4:
            # print(request.data["answer_text"])
            request.session['student_department'] = request.data["answer_text"]
            student_department = request.session.get("student_department")
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
 
                next_stage = int(current_stage) + 1
                stinged_next_stage = str(next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                next_question_completed = "Your department has been noted "+"( "+ student_department+" ). " + next_stage_question.question_text + '.'
                return Response({"status": "success", "question_text": next_question_completed, "stage":"4", "next_stage":"5", "from":"bot"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a matric number'
                return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)

        if stage_id == 5:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
                have_you_started_reg = serializer.data['answer_text']
                if have_you_started_reg.lower()=="yes":
                    next_stage = int(current_stage) + 1
                    stinged_next_stage = str(next_stage)
                    next_stage_question = Question.objects.get(stage = stinged_next_stage)
                    # print(next_stage_question.question_text)
                    next_question_completed = next_stage_question.question_text + '.'
                    # serializer.save()
                    # this would fetch wuestion 2 and return question 2
                    return Response({"status": "success", "question_text": next_question_completed, "stage":"5", "next_stage":"6", "from":"bot"}, status=status.HTTP_200_OK)
                
                elif have_you_started_reg.lower()=="no":
                    next_stage = int(current_stage) + 2
                    stinged_next_stage = str(next_stage)
                    next_stage_question = Question.objects.get(stage = stinged_next_stage)
                    # print(next_stage_question.question_text)
                    next_question_completed = next_stage_question.question_text + '.'
                    # serializer.save()
                    # this would fetch wuestion 2 and return question 2
                    return Response({"status": "success", "question_text": next_question_completed, "stage":"5", "next_stage":"7", "from":"bot"}, status=status.HTTP_200_OK)
                    

                else:
                    error_mesage = 'Did not get that, please reply with either yes or no'
                    return Response({"status": "error", "question_text": error_mesage, "from": "bot", "stage":"5", "next_stage":"5", }, status=status.HTTP_200_OK)

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
                # next 
                student_name = request.session.get("students_name")
                student_department = request.session.get("student_department")
                student_matric = request.session.get("student_matric")
                student_level = request.session.get("student_level")


                stage_checked = check_stage(stage_number)
                print(stage_checked)

                summary = {
                    "next_stage":{stage_checked},
                    "student_name": {student_name},
                    "student_level":{student_level},
                    "student_department":{student_department},
                    "student_matric":{student_matric},

                }
                summary = f"Summary {stage_checked} ! Student Name: {student_name}. Student Level: {student_level}. Student Department: {student_department}. Student Matric: {student_matric}"
                
                if stage_checked is None:
                    error_mesage = f'Sorry no stage with the character {stage_number} found enter from stage 1 to stage 7'
                    return Response({"status": "error", "question_text": error_mesage, "from":"bot", "stage":"6", "next_stage":"6"}, status=status.HTTP_200_OK)
                else:
                    # next_question_completed = {stage_checked}
                    return Response({"status": "success", "question_text": summary, "stage":"6", "next_stage":"00", "from":"bot"}, status=status.HTTP_200_OK)
                    # stage_checked


        if stage_id == 7:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
                next_stage = int(current_stage)
                stinged_next_stage = str(next_stage)
                next_stage_question = Question.objects.get(stage = stinged_next_stage)
                # print(next_stage_question.question_text)
                next_question_completed = "Goodbye!!"

                # serializer.save()
                # this would fetch wuestion 2 and return question 2
                return Response({"status": "success", "question_text": next_question_completed, "stage":"7", "next_stage":"00", "from":"bot"}, status=status.HTTP_200_OK)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a correct name'
                return Response({"status": "error", "question_text": error_mesage, "stage":"7", "next_stage":"7", "from":"bot"}, status=status.HTTP_200_OK)
        


        if stage_id == 11:
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                current_stage = serializer.data['stage']
                do_you_want_to_reg = serializer.data['answer_text']

                if do_you_want_to_reg.lower()=="yes":
                    stage_at = Stages.objects.filter(stage = "1").first()
                    return Response({"status": "success", "data": stage_at.stage_instruction, "stage":"11", "next_stage":"00"}, status=status.HTTP_200_OK)
                
                elif do_you_want_to_reg.lower()=="no":
                    message = "Okay, Bye "
                    return Response({"status": "success", "data": message, "stage":"11", "next_stage":"00"}, status=status.HTTP_200_OK)


                else:
                    error_mesage = 'Did not get that, please reply with either yes or no'
                    return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)
            else:
                error_mesage = 'Could not undestand what you just typed, please enter a correct answer'
                return Response({"status": "error", "data": error_mesage}, status=status.HTTP_400_BAD_REQUEST)
                