from rest_framework import serializers
from .models import Blog, Comment, Reaction


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'user', 'reaction_type', 'created_at', 'blog_post',
                  'comments']

    def validate(self, data):
        """
        Validate that either `blog_post` or `comment` is provided, but not both.
        """
        blog_post = data.get('blog_post')
        comment = data.get('comment')

        if not blog_post and not comment:
            raise serializers.ValidationError("Either 'blog_post' or 'comment' must be provided.")

        if blog_post and comment:
            raise serializers.ValidationError("Provide either 'blog_post' or 'comment', not both.")

        return data


class BlogSerializer(serializers.ModelSerializer):
    blog_reactions = ReactionSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'created_at',
                  'blog_reactions']


class CommentSerializer(serializers.ModelSerializer):
    comment_reactions = ReactionSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at', 'blog',
                  'comment_reactions']
