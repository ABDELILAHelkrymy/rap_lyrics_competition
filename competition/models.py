from django.db import models
import uuid


class Competition(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    

class CompetitionEntry(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='entries')
    rapper = models.ForeignKey('home.Rapper', on_delete=models.CASCADE, related_name='competitor')
    song = models.ForeignKey('home.Song', on_delete=models.CASCADE, related_name='song')
    recommandations = models.ManyToManyField('home.Recommandations', related_name='recommandations_for_comp')
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False)

    def __str__(self):
        return self.name
