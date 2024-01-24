from django.db import models
from django.contrib.auth.models import User

class ExampleModel(models.Model):
    # Basic Fields
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='uploads/')
    image_field = models.ImageField(upload_to='images/')

    # Relational Fields with unique related_name
    foreign_key_field = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='examplemodel_foreign_keys'
    )
    many_to_many_field = models.ManyToManyField(
        User, related_name='examplemodel_many_to_manys'
    )
    one_to_one_field = models.OneToOneField(
        User, on_delete=models.CASCADE, 
        related_name='examplemodel_one_to_ones'
    )

    # Other Fields
    url_field = models.URLField()
    uuid_field = models.UUIDField()
    choice_field = models.CharField(
        max_length=2, choices=[('A', 'Choice A'), ('B', 'Choice B')]
    )
    slug_field = models.SlugField()
    binary_field = models.BinaryField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    duration_field = models.DurationField()
    ip_address_field = models.GenericIPAddressField(protocol='IPv4')
    json_field = models.JSONField()
    validated_field = models.IntegerField()

    def __str__(self):
        return self.char_field



