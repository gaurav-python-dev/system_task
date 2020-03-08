
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
# from accounts.views import base_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", TemplateView.as_view(template_name="base.html"), name="home"),
    url(r'accounts/',include('django.contrib.auth.urls')),
    # url(r'^dblist/',base_view,name='basic'),
    url(r"^users/",include("accounts.urls", namespace="users")),
    url(
        r"^products/",
        include("products.urls", namespace="products"),
    ),

]