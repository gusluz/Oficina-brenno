# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True, blank=True)

#     USERNAME_FIELD = 'email'  # Define 'email' como identificador principal
#     REQUIRED_FIELDS = []  # Remove campos adicionais obrigatórios

#     def save(self, *args, **kwargs):
#         if not self.username:  # Se o username não foi definido
#             self.username = self.email
#         super().save(*args, **kwargs)
