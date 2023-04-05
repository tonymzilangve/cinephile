# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import viewsets, filters, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
#
# from custom_auth.jwt import JWTAuthentication
#
# from feedback.models import Comment
# from feedback.serializers import CommentSerializer, PostCommentSerializer
# from .pagination import CustomPageNumberPagination
# from .permissions import AuthorAllStaffAll, AuthorAllStaffAllButEdit
# from .serializers import *
#
#
# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     pagination_class = CustomPageNumberPagination
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [AuthorAllStaffAll]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#
#     filterset_fields = ['author', 'timestamp']
#     search_fields = ['id', 'title', 'author', 'text']
#     ordering_fields = ['id', 'author', 'timestamp']
#
#     def create(self, request, *args, **kwargs):
#         serializer = NewsSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save(author=self.request.user)
#             return Response(serializer.data)
#
#     @action(
#         detail=True,
#         methods=['get', 'post'],
#         permission_classes=[AuthorAllStaffAllButEdit],
#         serializer_class=PostCommentSerializer
#     )
#     def comments(self, request, pk=None):
#         if self.request.method == 'GET':
#             news = self.get_object()
#             comments = news.comments.all()
#             serializer = CommentSerializer(comments, many=True)
#
#             return Response(serializer.data)
#
#         if self.request.method == 'POST':
#             news = self.get_object()
#             serializer = PostCommentSerializer(data=request.data)
#             if serializer.is_valid():
#                 author = request.user
#                 text = serializer.data['text']
#                 Comment.objects.create(news=news, author=author, text=text)
#
#                 comments = news.comments.all()
#                 serializer = CommentSerializer(comments, many=True)
#
#                 return Response(serializer.data, status=201)
#
#     @action(
#         detail=True,
#         methods=['get', 'put', 'patch', 'delete'],
#         permission_classes=[AuthorAllStaffAllButEdit],
#         name='Comment',
#         url_path='comments/(?P<id>\d+)',
#         serializer_class=PostCommentSerializer
#     )
#     def get_comment(self, request, id=None, pk=None):
#         if self.request.method == 'GET':
#             comment = Comment.objects.get(pk=id)
#             serializer = CommentSerializer(comment)
#
#             return Response(serializer.data)
#
#         if self.request.method in ['PUT', 'PATCH']:
#             serializer = PostCommentSerializer(data=request.data)
#             if serializer.is_valid():
#                 text = serializer.data['text']
#                 comment = Comment.objects.get(pk=id)
#                 comment.text = text
#                 comment.save()
#                 return Response(serializer.data)
#
#         if self.request.method == 'DELETE':
#             comment = Comment.objects.get(pk=id)
#             comment.delete()
#
#             return Response(status=status.HTTP_200_OK)
#
#     @action(detail=True, methods=['get'], url_path='you-liked', url_name='liked')
#     def like_this_news(self, request, pk=None):
#         news = self.get_object()
#         user = request.user
#
#         if not user in news.who_liked.all():
#             news.who_liked.add(user)
#             msg = {'Liked': 'Ваш лайк принят!', '______': '______'}
#         else:
#             news.who_liked.remove(user)
#             msg = {'Unliked': 'Вы убрали свой лайк!', '______': '______'}
#
#         news.save()
#         serializer = NewsSerializer(news)
#         return Response({**msg, **serializer.data})
#
