from rest_framework import serializers
# from django.contrib.auth.models import User

from account.models import Author, User


class AuthorRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=64, write_only=True)
    email = serializers.EmailField(max_length=50, write_only=True)
    telegram_chat_id = serializers.IntegerField(write_only=True)
    password = serializers.CharField(max_length=64, write_only=True)
    password_2 = serializers.CharField(max_length=64, write_only=True)


    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['user', ]

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def create(self, validated_data):
        try:
            new_user = User(username=validated_data['username'],
                            email=validated_data['email'],
                            telegram_chat_id=validated_data['telegram_chat_id'],)
            new_user.set_password(validated_data['password'])
            new_user.save()
        except Exception as e:
            raise serializers.ValidationError(e)
        else:
            new_author = Author.objects.create(
                user=new_user
            )
            new_author.save()
            return new_author
