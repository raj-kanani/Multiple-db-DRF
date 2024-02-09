from rest_framework import serializers
from .models import Administrator
from .middleware import CustomMiddleware


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'

    # custom middleware code
    # def create(self, validated_data):
    #     current_user = CustomMiddleware.get_current_user(self.context.get('request'))
    #     print("current-user@@@@=", current_user)
    #
    #     if current_user:
    #         validated_data['username'] = current_user.username
    #         return super().create(validated_data)
    #     else:
    #         raise serializers.ValidationError("User not authenticated")
    #
    # def update(self, instance, validated_data):
    #     current_user = CustomMiddleware.get_current_user(self.context.get('request'))
    #     print("update-current-user@@@@=", current_user)
    #     if current_user:
    #         validated_data['username'] = current_user.username
    #         return super().update(instance, validated_data)
    #     else:
    #         raise serializers.ValidationError("User not authenticated")

    # multiple database code
    def create(self, validated_data):
        
        create_admins = Administrator.objects.create(
            username=validated_data['username'],
            email = validated_data['email'],
            password=validated_data['password']
        )
        return create_admins
