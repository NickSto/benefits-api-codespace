from programs.models import Program, Navigator, UrgentNeed
from rest_framework import viewsets, mixins
from rest_framework import permissions
from programs.serializers import ProgramSerializer, NavigatorAPISerializer, UrgentNeedAPISerializer


class ProgramViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows programs to be viewed or edited.
    """

    queryset = Program.objects.filter(active=True)
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class NavigatorViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows programs to be viewed or edited.
    """

    queryset = Navigator.objects.all()
    serializer_class = NavigatorAPISerializer
    permission_classes = [permissions.IsAuthenticated]


class UrgentNeedViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows programs to be viewed or edited.
    """

    queryset = UrgentNeed.objects.filter(active=True)
    serializer_class = UrgentNeedAPISerializer
    permission_classes = [permissions.IsAuthenticated]
