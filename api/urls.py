from django.urls import path
from api.views import (
    DjTinderDetail,
    DjTinderList,
    fetch_djtinder_proposals_for
)

urlpatterns = [
    path('djtinderusers/',
         DjTinderList.as_view(), name="djtinderuser-list"),
    path('djtinderusers/<int:pk>',
         DjTinderDetail.as_view(),
         name="djtinderuser-detail"),
    path('fetch_djtinder_proposals_for/<nick_of_finder>/<current_latitude>/<current_longitiude>/',
        fetch_djtinder_proposals_for, name='djtinder_proposals'),

]

