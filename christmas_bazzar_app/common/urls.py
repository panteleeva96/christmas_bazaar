from django.urls import path

from common.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index')
]
