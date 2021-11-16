from django.db import models
from datetime import datetime


class Voter (models.Model):

    """
    The vote info
        .. First name
        .. Surname
        .. national_id
        .. voter_id
        .. email_address
        ..
    """
    _id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=12, blank=True, null=True, unique=True)
    email_address = models.EmailField(unique=True)
    voter_id = models.CharField(default=str(abs(datetime.now().__hash__())), unique=True, max_length=30)
    time_created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.first_name} {self.surname}'


class Candidate (models.Model):

    _id = models.AutoField(primary_key=True)
    voter_id = models.OneToOneField('Voter', on_delete=models.CASCADE, unique=True)
    candidate_id = models.CharField(default=str(abs(datetime.now().__hash__())), unique=True,  max_length=30)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.voter_id.first_name} {self.voter_id.surname}'


class Vote (models.Model):

    voter_id = models.OneToOneField('Voter', on_delete=models.CASCADE, unique=True)
    candidate_id = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    time_cast = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Vote by {self.voter_id} to {self.candidate_id}'



