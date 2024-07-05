from django.db import models
from django.utils import timezone
# class Lead(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     country = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.email})"
class Pdf(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)  # Add this field
    pdf_file_name = models.CharField(default="complications-and-verification-process", max_length=1000)
    def __str__(self):
        return f"{self.pdf_file_name}"
    def get_pdf_url(self):
        if self.pdf_file:
            return self.pdf_file.url
        return None
    
class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    pdf = models.ForeignKey(Pdf, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email}) {self.country}"
    
