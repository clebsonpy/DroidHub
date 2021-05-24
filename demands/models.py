from django.contrib.auth.models import User
from django.utils import timezone as tz
from django.db import models


# Create your models here.
class Address(models.Model):
    cep = models.CharField(verbose_name='CEP', max_length=25,
                           null=False, blank=False
                           )
    address = models.CharField(verbose_name='Logradouro', max_length=250,
                               null=False, blank=False
                               )
    number = models.IntegerField(verbose_name='Número',
                                 null=False, blank=False
                                 )
    city = models.CharField(verbose_name='Cidade', max_length=250,
                            null=False, blank=False
                            )
    state = models.CharField(verbose_name='Estado', max_length=150,
                             null=False, blank=False
                             )
    country = models.CharField(verbose_name='País', max_length=150,
                               null=False, blank=False
                               )

    class Meta:
        verbose_name = 'Endereço'

    def __str__(self):
        return '{} - {}'.format(self.cep, self.city)


class Demands(models.Model):
    status_choice = (
        ('open', 'Aberto'),
        ('finish', 'Finalizada')
    )
    user = models.ForeignKey(verbose_name='Usuário', to=User,
                             null=False, blank=False, on_delete=models.CASCADE,
                             related_name='demands_user'
                             )
    address = models.OneToOneField(verbose_name='Endereço', to=Address,
                                   null=False, blank=False, on_delete=models.PROTECT,
                                   related_name='demands_address'
                                   )
    description = models.TextField(verbose_name='Descrição',
                                   null=False, blank=False
                                   )
    status = models.CharField(verbose_name='Status', max_length=20,
                              null=False, blank=False,
                              choices=status_choice,
                              )
    date_open = models.DateField(verbose_name='Data de abertura',
                                 null=False, blank=False, default=tz.now
                                 )
    date_finish = models.DateField(verbose_name='Data de finalização',
                                   null=None, blank=False, default=None
                                   )

    class Meta:
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'

    def __str__(self):
        return '{} - {}'.format(self.user, self.description[:150])
