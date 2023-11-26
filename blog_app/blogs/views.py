from django.shortcuts import render
from django.views import View

# Create your views here.
from django.http import HttpResponse


class IndexView(View):
    def get(self, request):
        return render(request, 'blogs/index.html')


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Blog, Comment, Reaction
from .serializers import BlogSerializer, CommentSerializer, ReactionSerializer
from rest_framework.permissions import IsAuthenticated


class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def react_to_blog(self, request, pk=None):
        blog = Blog.objects.get(pk=pk)
        user = request.user
        reaction_type = request.data.get('reaction_type')

        return self.react(user, blog, reaction_type)

    @action(detail=True, methods=['post'])
    def react_to_comment(self, request, pk=None):
        comment = Comment.objects.get(pk=pk)
        user = request.user
        reaction_type = request.data.get('reaction_type')

        return self.react(user, comment, reaction_type)

    def react(self, user, target_instance, reaction_type):
        if reaction_type not in [Reaction.LIKE, Reaction.DISLIKE]:
            return Response({'error': 'Invalid reaction_type'}, status=status.HTTP_400_BAD_REQUEST)

        reaction, created = Reaction.objects.get_or_create(user=user, target_instance=target_instance)
        reaction.reaction_type = reaction_type
        reaction.save()

        serializer = self.get_serializer(target_instance)
        return Response(serializer.data)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        blogs = self.get_queryset()
        return render(request, 'blogs/index.html', {'blogs': blogs})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
