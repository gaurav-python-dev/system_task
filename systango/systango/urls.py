from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'accounts/',include('django.contrib.auth.urls')),
    url(r"^users/",include("accounts.urls", namespace="users")),
    url(r"^products/",include("products.urls", namespace="products"),),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns