from django.urls import re_path, path, include
from django.views.generic import TemplateView

from core.utils.urls import urlpatterns

urlpatterns += [
    path('api/v1/', include('user.urls')),

    re_path(r'(login|register).*', TemplateView.as_view(template_name='auth.html')),
    re_path(r'', TemplateView.as_view(template_name='main.html')),
]
