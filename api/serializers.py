from rest_framework import serializers
from .models import CustomUser

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # optional for update
    class Meta:
        model = CustomUser
        fields = ["id", "name", "username", "email", "password", "is_staff", "is_superuser"]
        extra_kwargs = {
            "id": {"read_only": True}
        }

    def create(self, validated_data):
        user = CustomUser(
            name=validated_data["name"],
            username=validated_data["username"],
            email=validated_data["email"],
            is_staff=validated_data.get("is_staff", False),
            is_superuser=validated_data.get("is_superuser", False)
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Handle password separately
        password = validated_data.pop("password", None)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Only set new password if provided
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance