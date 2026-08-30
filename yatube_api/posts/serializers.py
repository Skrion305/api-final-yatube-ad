from rest_framework import serializers
from .models import Post, Comment, Group, Follow, User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group')
        read_only_fields = ('id', 'author', 'pub_date')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('id', 'author', 'created', 'post')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('user',)

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                {'following': 'Нельзя подписаться на самого себя!'}
            )
        if Follow.objects.filter(user=self.context['request'].user, following=data['following']).exists():
            raise serializers.ValidationError(
                {'following': 'Вы уже подписаны на этого пользователя.'}
            )
        return data