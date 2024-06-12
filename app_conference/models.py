from django.db import models


# Create your models here.
class LogoModel(models.Model):
    logo_image = models.ImageField(upload_to="static/Logo")

    def __str__(self):
        return self.logo_image

    class Meta:
        db_table = 'logo'


class ConferenceModel(models.Model):
    conference_title = models.CharField(max_length=1000)
    conference_description = models.TextField()
    conference_logo = models.ForeignKey(LogoModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.conference_title

    class Meta:
        db_table = 'conferences'
