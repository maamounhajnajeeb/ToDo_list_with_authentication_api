from rest_framework import serializers

from django.contrib.auth import authenticate, get_user_model


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
        )
    password = serializers.CharField(
        label="Password", write_only=True
        , trim_whitespace=False,
        )
    
    def validate(self, attrs):
        username, password = attrs.get("username"), attrs.get("password")
        
        if not (username or password):
            raise serializers.ValidationError(
                'Both "username" and "password" are required.',
                code='authorization'
            )
        
        user = authenticate(
            request=self.context.get("request"), 
            username=username, password=password)
        
        if not user:
            raise serializers.ValidationError(
                "Access denied: wrong username or password.",
                code="authorization"
            )
        
        attrs["user"] = user
        return attrs


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64, min_length=6, write_only=True)
    email = serializers.CharField(max_length=64, min_length=12,)
    password = serializers.CharField(max_length=64, min_length=6,)
    phone_number = serializers.IntegerField()
    
    username_err_msg = {
        "username" : "Username should contain alphanumeric characters only (letters and numbers)"
    }
    
    username_repeat_err = {
        "username": "This Username is already exists"
    }
    
    email_err_msg = {
        "username": "This Email already exists"
    }
    
    def validate(self, attrs):
        username, email = attrs.get("username"), attrs.get("email")
        
        if not username.isalnum():
            raise serializers.ValidationError(
                self.username_err_msg
            )
        
        repeated_username = get_user_model().objects.filter(username=username)
        if repeated_username.exists():
            raise serializers.ValidationError(
                self.username_repeat_err
            )
        
        repeated_email = get_user_model().objects.filter(email=email)
        if repeated_email.exists():
            raise serializers.ValidationError(
                self.email_err_msg
            )
        
        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user


class ProfileSerializer(serializers.Serializer):
    
    class Meta:
        model = get_user_model()
        fields = (
            "id", "username", "email", "phone_number", ""
        )
