from django.conf.urls import url
from shop import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    url(r'^(?P<shop_id>\d+)/$', views.detail, name='detail'),
    url('new_shop', views.post_new, name='post_new'),
]
