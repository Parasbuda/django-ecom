from wsgiref.validate import validator
import black
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

# Create your models here.


def upload_photo(instance, filename):
    # return "/".join(["supplier", filename])
    return f"supplier/{filename}"


def validate_photo(image):
    file_size = image.size
    limit_byte_size = settings.MAX_UPLOAD_SIZE
    if file_size > limit_byte_size:
        f = limit_byte_size / 1024
        f = f / 1024
        raise ValidationError("Max size of the file is %s MB" % f)


class Supplier(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to=upload_photo, validators=[validate_photo], blank=True
    )
    created_date = models.DateField(blank=True)

    def save(self, *args, **kwargs):
        date = timezone.now()
        self.created_date = date
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
