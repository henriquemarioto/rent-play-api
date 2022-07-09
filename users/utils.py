from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(
        self,
        email,
        first_name,
        nickname,
        last_name,
        password,
        is_superuser,
        **extra_fields
    ):
        now = timezone.now()

        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            nickname=nickname,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(
        self, email, nickname, first_name, last_name, password, **extra_fields
    ):
        return self._create_user(
            email, nickname, first_name, last_name, password, False, **extra_fields
        )

    def create_superuser(
        self, email, nickname, first_name, last_name, password, **extra_fields
    ):
        return self._create_user(
            email,
            nickname,
            first_name,
            last_name,
            password,
            False,
            True,
            **extra_fields
        )
