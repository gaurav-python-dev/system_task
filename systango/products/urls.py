from django.conf.urls import url

from . import views

app_name = "products"
urlpatterns = [
    url(r"^$", views.ProductList.as_view(), name="list"),
    url(r"^create/$", views.ProductCreate.as_view(), name="create"),
    url(r"^(?P<db>[\w.@+-]+)/update/(?P<pk>\d+)/$", views.ProductUpdate.as_view(), name="update"),
    url(r"^(?P<db>[\w.@+-]+)/delete/(?P<pk>\d+)/$", views.ProductDelete.as_view(), name="delete"),
]
