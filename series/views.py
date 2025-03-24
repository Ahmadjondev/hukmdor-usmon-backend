from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from series.models import Episode, Series, Casts
from series.serializers import EpisodeSerializer, SeriesSerializer, CastsSerializer


# Create your views here.

class SeriesView(APIView):
    def get(self, request):
        series = Series.objects.all().first()
        serializer = SeriesSerializer(series)
        return Response(serializer.data)


# For Admin
# class SeriesViewSet(viewsets.ModelViewSet):
#     queryset = Series.objects.all()
#     serializer_class = SeriesSerializer
#     permission_classes = [IsAdminUser, IsAuthenticated]


class EpisodesView(APIView):
    def get(self, request):
        episode = Episode.objects.all()
        serializer = EpisodeSerializer(episode, many=True)
        return Response(serializer.data)


# For Admin
# class EpisodesViewSet(viewsets.ModelViewSet):
#     queryset = Episode.objects.all()
#     serializer_class = EpisodeSerializer
#     permission_classes = [IsAdminUser, IsAuthenticated]
#

class CastsView(ListAPIView):
    queryset = Casts.objects.all()
    serializer_class = CastsSerializer


# class AdminLoginView(APIView):
#     permission_classes = [AllowAny]
#
#     @swagger_auto_schema(
#         operation_description="Admin login endpoint",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
#                 'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
#             },
#             required=['username', 'password']
#         ),
#         responses={
#             200: openapi.Response('Token', openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'token': openapi.Schema(type=openapi.TYPE_STRING, description='Token')
#                 }
#             )),
#             401: "Invalid credentials",
#             403: "User is not an admin"
#         }
#     )
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None and user.is_active and user.is_staff:
#             data = login(request, user)
#             res = Response()
#             res.data = {'detail': 'Login successful'}
#             # res.headers['Set-Cookie'] = 'sessionid={}; HttpOnly; Path=/; SameSite=Lax'.format(data.session_key)
#             # res.headers['Set-Cookie'] = 'csrftoken={}; HttpOnly; Path=/; SameSite=Lax'.format(data.csrf_token)
#             return res
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#
# class TokenExpireCheckView(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request):
#         session_key = request.session.session_key
#         csrf_token = request.COOKIES.get('csrftoken')
#
#         if not session_key:
#             return Response({'error': 'Session ID not found'}, status=status.HTTP_403_FORBIDDEN)
#         try:
#             session = Session.objects.get(session_key=session_key)
#         except Session.DoesNotExist:
#             return Response({'error': 'Session does not exist'}, status=status.HTTP_403_FORBIDDEN)
#
#         if session.expire_date < timezone.now():
#             return Response({'error': 'Session has expired'}, status=status.HTTP_403_FORBIDDEN)
#
#         if not csrf_token:
#             return Response({'error': 'CSRF token not found'}, status=status.HTTP_403_FORBIDDEN)
#
#         return Response({'detail': 'Session and CSRF token are valid'}, status=status.HTTP_200_OK)
