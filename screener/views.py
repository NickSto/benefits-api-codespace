from django.shortcuts import render
from django.http import HttpResponse
from screener.models import Screen, IncomeStream, Expense
from rest_framework import viewsets, views
from rest_framework import permissions
from rest_framework.response import Response
from screener.serializers import ScreenSerializer, IncomeStreamSerializer, ExpenseSerializer, EligibilitySerializer
from programs.models import Program

def index(request):
    return HttpResponse("Colorado Benefits Screener API")

class ScreenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows screens to be viewed or edited.
    """
    queryset = Screen.objects.all().order_by('-submission_date')
    serializer_class = ScreenSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['has_income', 'agree_to_tos']


class IncomeStreamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows income streams to be viewed or edited.
    """
    queryset = IncomeStream.objects.all()
    serializer_class = IncomeStreamSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['screen']


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows expenses to be viewed or edited.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['screen']


class EligibilityView(views.APIView):

    def get(self, request, id):
        all_programs = Program.objects.all()
        screen = Screen.objects.get(pk=id)

        data = []
        for program in all_programs:
            eligibility = program.eligibility(screen)
            data.append({"program_name": program.programName, "eligible": eligibility["eligible"], "value": eligibility["value"]})
        results = EligibilitySerializer(data, many=True).data
        return Response(results)