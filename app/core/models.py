from django.db import models


class Wedding(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    image = models.CharField(max_length=255, default='https://images.unsplash.com/reserve/xd45Y326SvKzSR3Nanc8_MRJ_8125-1.jpg?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Guest(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_wedding_id(self):
        return self.wedding.id

    def all_guests_given_wedding_id(self, id):
        return Guest.objects.filter(wedding_id=id)


class Photo(models.Model):
    number = models.CharField(max_length=3)
    description = models.CharField(max_length=255, blank=True)
    guest = models.ManyToManyField(Guest)

    def __str__(self):
        return self.number


class PhotoGuest(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WeddingGuest(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
