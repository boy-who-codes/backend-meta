from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import LeadForm
from .models import Lead
from leads.models import Lead  # Correct import for the 'leads' app
from django.http import HttpResponse
from main.views import *
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



def lead_form(request):
    seo_settings = SEO.objects.first()  # Fetch SEO settings
    footers = Footer.objects.all()
    menu_links = MenuLink.objects.filter(parent_link__isnull=True).order_by('order')

    if request.method == 'POST':
        form = LeadForm(request.POST, request.FILES)
        if form.is_valid():
            lead = form.save()

            # Prepare email
            subject = 'New Lead Submission'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['rahulsinhaoff@gmail.com']  # Change to your recipient email(s)

            context = {
                'lead': lead
            }

            # Render the email template with the context
            message = render_to_string('email/lead_email.html', context)
            email = EmailMessage(subject, message, from_email, recipient_list)
            email.content_subtype = 'html'  # Important to set the content type to HTML

            # Send email
            email.send()

            # Handle file download (if any logic is needed here)
            # Add your file download handling code here

            # Redirect or render a success page
            return redirect('lead_form')  # Replace 'success_page' with your actual success page or URL name

    else:
        form = LeadForm()

    return render(request, 'leads/lead_form.html', {
        'form': form,
        'menu_links': menu_links,
        'footers': footers,
        'seo': seo_settings,
    })

# def lead_form(request):
#     seo_settings = SEO.objects.first()  # Fetch SEO settings
#     footers = Footer.objects.all()
#     menu_links = MenuLink.objects.filter(parent_link__isnull=True).order_by('order')

#     if request.method == 'POST':
#         form = LeadForm(request.POST, request.FILES)
#         if form.is_valid():
#             lead = form.save()

#             # # Prepare email
#             # subject = 'New Lead Submission'
#             # message = f'Lead Details:\nFirst Name: {lead.first_name}\n Last name:{lead.last_name} \nEmail: {lead.email}\nCountry: {lead.country}\n Created at: {lead.created_at}\n Location: {lead.location}'
#             # from_email = settings.DEFAULT_FROM_EMAIL
#             # recipient_list = ['recipient@example.com']  # Change to your recipient email(s)

#             # # Send email
#             # send_mail(subject, message, from_email, recipient_list)
            
#             # Handle file download (assuming PDF)
#             # Add your file download handling code here
#             subject = 'New Lead Submission'
#             from_email = settings.DEFAULT_FROM_EMAIL
#             recipient_list = ['recipient@example.com']  # Change to your recipient email(s)
    
#             context = {
#                 'lead': lead
#                     }   
    
#             message = render_to_string('email/lead_email.html', context)
#             email = EmailMessage(subject, message, from_email, recipient_list)
#             email.content_subtype = 'html'  # Important to set the content type to HTML
    
#     # Send email
#             email.send()

#     else:
#         form = LeadForm()
    
#     return render(request, 'leads/lead_form.html', {
#         'form': form,
#         'menu_links': menu_links,
#         'footers': footers,
#         'seo': seo_settings,
#     })



# def lead_form(request):
#     seo_settings = SEO.objects.first()  # Fetch SEO settings
#     footers = Footer.objects.all()
#     menu_links = MenuLink.objects.filter(parent_link__isnull=True).order_by('order')

#     if request.method == 'POST':
#         form = LeadForm(request.POST, request.FILES)
#         if form.is_valid():
#             lead = form.save()
#             # Handle file download (assuming PDF)
        
           
#     else:
#         form = LeadForm()
#     return render(request, 'leads/lead_form.html', {'form': form,
#                                                     'menu_links': menu_links,
#                                             'footers': footers,
#                                             'seo': seo_settings,
#                                                     })

@user_passes_test(lambda u: u.is_superuser)
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})