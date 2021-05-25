from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField('E-mail', unique=True)


class Profile(models.Model):
    user = models.OneToOneField(verbose_name='Usuário', to=User,
                                on_delete=models.CASCADE
                                )
    cpf_cnpj = models.CharField(verbose_name='CPF/CNPJ', max_length=14,
                                null=False, blank=False,
                                )
    phone = models.CharField(verbose_name='Telefone/Celular', max_length=15,
                             null=False, blank=False,
                             )
    address = models.OneToOneField(verbose_name='Endereço', to='demands.Address',
                                   on_delete=models.PROTECT, related_name='user_address',
                                   null=False, blank=False,
                                   )

    def __str__(self):
        return self.user.username
