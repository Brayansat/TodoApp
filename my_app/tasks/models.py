from django.db import models
#Class user
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.TextField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def str(self):
        return f"{self.username} {self.email} {self.first_name} {self.last_name}"


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def str(self):
        return f"{self.name} {self.description}"