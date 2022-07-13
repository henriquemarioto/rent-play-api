from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(
        self,
        nickname,
        first_name,
        last_name,
        cellphone,
        email,
        password,
        is_superuser,
        **extra_fields
    ):
        now = timezone.now()

        email = self.normalize_email(email)

        user = self.model(
            nickname=nickname,
            first_name=first_name,
            last_name=last_name,
            cellphone=cellphone,
            email=email,
            wallet=0,
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
        self,
        email,
        nickname,
        cellphone,
        first_name,
        last_name,
        password,
        **extra_fields
    ):
        return self._create_user(
            nickname,
            first_name,
            last_name,
            cellphone,
            email,
            password,
            False,
            **extra_fields
        )

    def create_superuser(
        self,
        email,
        nickname,
        cellphone,
        first_name,
        last_name,
        password,
        **extra_fields
    ):
        return self._create_user(
            nickname,
            first_name,
            last_name,
            cellphone,
            email,
            password,
            True,
            **extra_fields
        )
