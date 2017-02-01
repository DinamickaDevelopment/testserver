# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from homepage.models import Post, Contact
import json
from django.conf import settings
from mailjet_rest import Client
from zopy.crm import CRM
# from articles.models import Article

class HomePageView(TemplateView):

    template_name = "index.pug"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class AboutView(TemplateView):

    template_name = "about.pug"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class HistoryView(TemplateView):

    template_name = "history.pug"

    def get_context_data(self, **kwargs):
        context = super(HistoryView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class ServicesView(TemplateView):

    template_name = "services.pug"

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class OPECView(TemplateView):

    template_name = "opec.pug"

    def get_context_data(self, **kwargs):
        context = super(OPECView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class SovietView(TemplateView):

    template_name = "soviet.pug"

    def get_context_data(self, **kwargs):
        context = super(SovietView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class CountryView(TemplateView):

    template_name = "country.pug"

    def get_context_data(self, **kwargs):
        context = super(CountryView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class ContactView(TemplateView):

    template_name = "contact.pug"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class PostsView(TemplateView):

    template_name = "posts.pug"

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by("-created")
        return context


class PostView(TemplateView):

    template_name = "post.pug"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, id=kwargs.get('post_id'))

        return context


def contact_form_handler(request):
# {first_name: "test", last_name: "test", email: "test@test.com", company: "test", phone: "",…}
    # print request.POST
    try:
        payload = json.loads(request.body)
        if payload.get('first_name') and payload.get('last_name') and payload.get('email'):
            #save to database
            Contact.objects.create(
                first_name=payload.get('first_name'),
                last_name=payload.get('last_name'),
                email=payload.get('email'),
                company=payload.get('company'),
                phone=payload.get('phone'),
                comment=payload.get('comment'))
            
            # send email
            mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET))
            email = {
                'FromName': '%s %s' % (payload.get('first_name'), payload.get('last_name')),
                'FromEmail': 'subscribers@petro-logistics.com',
                'Reply-to': payload.get('email'),
                'Subject': 'Petro-Logistics contact form',
                'Text-Part': 'Contact form data: \nFirst name: %s \nLast name: %s \nEmail: %s \nCompany: %s \nPhone: %s \nComment: %s' % (payload.get('first_name'), payload.get('last_name'), payload.get('email'), payload.get('company'), payload.get('phone'), payload.get('comment')),
                'Recipients': [{'Email': 'info@petro-logistics.com'}, {'Email': 'info@canterburycomputers.com'}]
            }

            mailjet.send.create(email)

            crm = CRM(authToken=settings.ZOHO_AUTH_TOKEN, scope="ZohoCRM/crmapi")

            leadData = {
                "First Name" : payload.get('first_name'),
                "Last Name" : payload.get('last_name'),
                "Company" : payload.get('company'),
                "Lead Owner" : "daniel.gerber@petro-logistics.com",
                'Email': payload.get('email'),
                'Phone': payload.get('phone'),
                "Lead Source" : "Website contact form",
                "Description" : payload.get('comment')
            }
            crm_insert = crm.insertRecords(module="Leads", xmlData=[leadData], version=2, duplicateCheck=2)
            print crm_insert.data
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "required field missing"})
    except Exception, e:
        print e
        return JsonResponse({"status": "error"}) 