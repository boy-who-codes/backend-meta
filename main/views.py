from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import*
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail


def page_detail(request, slug):
    seo_settings = SEO.objects.first()  # Fetch SEO settings
    footers = Footer.objects.all()
    menu_links = MenuLink.objects.filter(parent_link__isnull=True).order_by('order')
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page,
                                                'menu_links': menu_links,
                                            'footers': footers,
                                            'seo': seo_settings,
                                                })

def base(request):
    seo_settings = SEO.objects.first()  # Fetch SEO settings
    footers = Footer.objects.all()
    menu_links = MenuLink.objects.filter(parent_link__isnull=True).order_by('order')
    return render(request, 'base.html', {'menu_links': menu_links,
                                            'footers': footers,
                                            'seo': seo_settings,
                                          })
    
def index(request):
    seo_settings = SEO.objects.first()  # Fetch SEO settings
    footers = Footer.objects.all()
    menu_links = MenuLink.objects.filter(parent_link__isnull=True).order_by('order')
    clients = ClientLogo.objects.all()
    numbers = Numbers.objects.all()
    abouts = About.objects.all()
    services = Services.objects.all()
    testimonials = Testimonial.objects.all()

    form_submitted = False  # Initialize form submission status

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save contact message to database
            contact_message = ContactMessage(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact_message.save()

            # Send email notification
            send_mail(
                'Contact Form Submission',
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['your_email@example.com'],  # List of recipients
                fail_silently=False,
            )

            form_submitted = True  # Update form submission status
    else:
        form = ContactForm()

    # Render the index.html template with context data
    return render(request, 'index.html', {
        'form': form,
        'clients': clients,
        'numbers': numbers,
        'abouts': abouts,
        'services': services,
        'testimonials': testimonials,
        'menu_links': menu_links,
        'footers': footers,
        'seo': seo_settings,
        'form_submitted': form_submitted,  # Pass form submission status to template
    })
    
# views.py

from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

