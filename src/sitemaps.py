from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from main.models import *
from leads.models import *

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)

class MyModelSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return MenuLink.objects.all() , Page.objects.all() , ContactMessage.objects.all() , ClientLogo.objects.all() , Numbers.objects.all() , About.objects.all() , Services.objects.all(), Footer.objects.all(), FooterLink.objects.all(), Testimonial.objects.all() , SEO.objects.all(), Lead.objects.all() ,Pdf.objects.all()

    def lastmod(self, obj):
        return obj.modified