from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django import forms
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'background_image_tag')

    def background_image_tag(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.background_image.url))
        return "-"
    background_image_tag.short_description = 'Background Image'

admin.site.register(Page, PageAdmin)

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_link_url', 'parent_link', 'has_submenu', 'order')
    list_filter = ('parent_link', 'has_submenu', 'separate_url')
    search_fields = ('title', 'url', 'page__title')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'page':
            kwargs['queryset'] = Page.objects.all()
        elif db_field.name == 'parent_link':
            kwargs['queryset'] = MenuLink.objects.filter(parent_link__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'message')
    search_fields = ('first_name', 'last_name', 'email', 'message')
    list_filter = ('email', )
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from django.utils.encoding import smart_str
        import datetime

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="contact_messages_{datetime.datetime.now().strftime("%Y-%m-%d")}.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Message'])

        for obj in queryset:
            writer.writerow([smart_str(obj.first_name), smart_str(obj.last_name), smart_str(obj.email), smart_str(obj.message)])

        return response

    export_to_csv.short_description = "Export to CSV"


class ClientLogoAdminForm(forms.ModelForm):
    class Meta:
        model = ClientLogo
        fields = ['client', 'image']

class ClientLogoAdmin(admin.ModelAdmin):
    form = ClientLogoAdminForm
    list_display = ('client', 'image_tag',)
    search_fields = ('client',)
    list_filter = ('client',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Image'

    def get_form(self, request, obj=None, **kwargs):
        form = super(ClientLogoAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['image'].widget.attrs.update({'multiple': 'multiple'})
        return form

admin.site.register(ClientLogo, ClientLogoAdmin)


class NumbersAdmin(admin.ModelAdmin):
    list_display = ('number', 'text',)

admin.site.register(Numbers, NumbersAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'paragraph',)

admin.site.register(About, AboutAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('text', 'page',)

admin.site.register(Services, ServicesAdmin)

class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1

class FooterAdmin(admin.ModelAdmin):
    list_display = ('address', 'logo_tag',)
    inlines = [FooterLinkInline]

    def logo_tag(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.logo.url))
        return "-"
    logo_tag.short_description = 'Logo'

admin.site.register(Footer, FooterAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'review')

admin.site.register(Testimonial, TestimonialAdmin)

class SEOAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Meta Tags', {
            'fields': ('meta_description', 'meta_keywords', 'meta_author')
        }),
        ('Open Graph (OG) Tags', {
            'fields': ('og_title', 'og_description', 'og_image')
        }),
        ('Progressive Web App (PWA) Settings', {
            'fields': ('pwa_enabled', 'pwa_name', 'pwa_short_name', 'pwa_description', 'pwa_icon')
        }),
        ('Other Settings', {
            'fields': ('favicon', 'apple_touch_icon')
        }),
       
        ('Custom Head Tags', {
            'fields': ('custom_head_tags',),
        }),
    )

admin.site.register(SEO, SEOAdmin)