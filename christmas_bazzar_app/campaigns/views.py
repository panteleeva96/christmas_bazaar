from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from campaigns.models import Campaign


class CampaignView(TemplateView):
    template_name = 'campaigns/campaign_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaign'] = Campaign.objects.first()

        return context
