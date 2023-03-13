from django.db import models

# Create your models here.

class Verb(models.Model):

    infinitif = models.CharField(max_length=30)
    translation = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.infinitif)
    

# class VerbUsage(models.Model):

#     # user = 
#     # session_id = 
#     # timestamp = 
#     # verb_id =
#     # tense = 
#     # POV = 
#     # success = (boolean)

