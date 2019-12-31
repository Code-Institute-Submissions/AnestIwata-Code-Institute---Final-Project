import stripe

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def makeDonation(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1500,
            currency='eur',
            description='A Django charge',
            source=request.POST['stripeToken']
        )

        user = request.user
        user.profile.donations += 15
        user.save()
        return render(request, 'charge.html')