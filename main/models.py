from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from leads.models import Lead  # Correct import for the 'leads' app

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    slug = models.SlugField(unique=True, blank=True)
    background_image = models.ImageField(upload_to='page_backgrounds/', blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
# class MenuLink(models.Model):
#     title = models.CharField(max_length=200)
#     page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)
#     parent_link = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
#     has_submenu = models.BooleanField(default=False)
#     order = models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.title

class MenuLink(models.Model):
    title = models.CharField(max_length=200)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)
    parent_link = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='submenus')
    has_submenu = models.BooleanField(default=False)
    separate_url = models.BooleanField(default=False)
    url = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=0)

    def get_link_url(self):
        if self.separate_url:
            return self.url
        elif self.page:
            return self.page.slug
        else:
            return '#'  # or any default URL for cases where no link is set

    def __str__(self):
        return self.title
    
    
class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} : {self.message}"

#Clients
class ClientLogo(models.Model):
    client = models.CharField(default='null' , max_length=10000)
    image = models.ImageField(upload_to='client_logos/')

    def __str__(self):
        return f"Logo for {self.client}"
    
class Numbers(models.Model):
    number = models.CharField(default='null', max_length=1000)
    text = models.TextField()

    def __str__(self):
        return f"{self.number} - {self.text}"
    
class About(models.Model):
    heading = models.CharField(max_length=200)
    paragraph = models.TextField()

    def __str__(self):
        return self.heading
    
 #Services
class Services(models.Model):
    text = models.CharField(max_length=200)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.text        
    
    
class Footer(models.Model):
    address = models.TextField()
    logo = models.ImageField(upload_to='footer_logos/')

    def __str__(self):
        return "Footer"

class FooterLink(models.Model):
    footer = models.ForeignKey(Footer, related_name='links', on_delete=models.CASCADE)
    link_text = models.CharField(max_length=200)
    link_url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.link_text} ({self.order})"   
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    review = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.organization})"
    
    
    
    
###########################serious stuff####################################
class SEO(models.Model):
    # Meta tags
    meta_description = models.CharField(max_length=255, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    meta_author = models.CharField(max_length=100, blank=True)

    # OG tags
    og_title = models.CharField(max_length=200, blank=True)
    og_description = models.CharField(max_length=255, blank=True)
    og_image = models.ImageField(upload_to='og_images/', blank=True)

    # PWA settings
    pwa_enabled = models.BooleanField(default=False)
    pwa_name = models.CharField(max_length=100, blank=True)
    pwa_short_name = models.CharField(max_length=50, blank=True)
    pwa_description = models.TextField(blank=True)
    pwa_icon = models.ImageField(upload_to='pwa_icons/', blank=True)

    # Other settings
    favicon = models.ImageField(upload_to='favicons/', blank=True)
    apple_touch_icon = models.ImageField(upload_to='apple_touch_icons/', blank=True)

    # New field for custom <head> tags
    custom_head_tags = models.TextField(blank=True, help_text="Enter any custom <head> tags here")

    
    def __str__(self):
        return "SEO Settings"     