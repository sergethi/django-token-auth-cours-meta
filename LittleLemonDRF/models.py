from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Sana = '8aebf0cb5422c2ee187d842f2bdcf371b42351ff'
# Mario = '1439bae1857d3d891336523b884f6b82fb9bd4a2'
# Adrian = 'b67dd4a8090a85e0b475925f87b7069d14e8fbac'