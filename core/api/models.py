from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

class Event(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField()
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)

    def __str__(self):
        return str(str(self.name) + ' - ' + str(self.date) + '  - Room: ' + str(self.room.id))
    
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(str(self.event.date) + '- Client: ' + self.user.username)