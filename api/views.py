from rest_framework import viewsets, permissions, filters
from rest_framework.authentication import TokenAuthentication
from .models import WebringModel
from .serializers import WebringSerializer

class WebringViewSet(viewsets.ModelViewSet):
    queryset = WebringModel.objects.all()
    serializer_class = WebringSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
