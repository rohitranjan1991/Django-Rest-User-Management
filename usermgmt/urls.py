from django.conf.urls import url
from django.urls import path

from usermgmt.apis import handle_user

urlpatterns = [
    url(r'^user$', handle_user),
    url(r'^user/(?P<user_id>\d+)$', handle_user),
]
