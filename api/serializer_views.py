from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from user.models import UserProfile
from rest_framework.permissions import IsAuthenticated


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = UserProfile.objects.filter(user_id=1)
    serializer_class = ProfileSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.request.query_params.get('id')
        return UserProfile.objects.filter(user_id=pk)
