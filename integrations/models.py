from django.db import models


class TestRunResults(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    body_test = models.JSONField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body_test)


class DroneCIListResults(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    number = models.CharField(max_length=255, verbose_name='Номер билда')
    status = models.CharField(max_length=255, verbose_name='Статус')
    autor_build = models.CharField(max_length=255, verbose_name='Автор запуска')
    date_run = models.DateTimeField(verbose_name='Дата запуска')

    def __str__(self):
        return str(self.number)

    def get_link_in_drone(self):
        return f'https://ci.idwell.tech/iDWELL/idwell-ui-tests/{self.id}'

