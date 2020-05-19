from rest_framework import serializers

from .models import UserProfile, Subjects, User


class ProfileSerializers(serializers.ModelSerializer):

    def create(self, validated_data):

        user = User.objects.create(
            first_name=self.initial_data['first_name'],
            last_name=self.initial_data['last_name'],
            email=self.initial_data['email'],
            username=self.initial_data['username']
        )
        users = UserProfile.objects.create(**validated_data)

        return users

    class Meta:
        model = UserProfile
        fields = '__all__'


class SubjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = '__all__'
