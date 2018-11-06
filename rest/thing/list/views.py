from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from thing.serializers import ThingSerializer
from thing.models import Thing, Recommended

class ListViewset(viewsets.ModelViewSet):
    serializer_class = ThingSerializer
    permission_classes_by_action = {
        'recommended': [permissions.AllowAny],
        'search': [permissions.AllowAny],
        'created_by': [permissions.IsAuthenticated],
        'applied_by': [permissions.IsAuthenticated],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def created_by(self, request):
        things = Thing.objects.filter(created_by=request.user)
        serializer = self.get_serializer(things, many=True)
        data = serializer.data
        return Response(data)

    def applied_by(self, request):
        things = Thing.objects.all()
        serializer = self.get_serializer(things, many=True)
        data = serializer.data
        return Response(data)

    def search(self, request):
        # search by category, name
        category_id = request.data.get('category_id')
        keyword = request.data.get('keyword')
        things = Thing.objects.all()
        if request.user.is_authenticated:
            things = things.exclude(created_by=request.user)
        if category_id is not None and category_id != '':
            things = things.filter(category_id=category_id)
        if keyword is not None and keyword != '':
            things = things.filter(name__contains=keyword)
        serializer = self.get_serializer(things, many=True)
        data = serializer.data
        return Response(data)

    def recommended(self, request):
        things = []
        recommendeds = Recommended.objects.all()
        for recommended in recommendeds:
            things.append(recommended.thing)

        serializer = self.get_serializer(things, many=True)
        data = serializer.data
        return Response(data)