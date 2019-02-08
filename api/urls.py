from django.urls import path
from api.views import (
    DjTinderDetail,
    DjTinderList,
    ProposalsApiView,
)

urlpatterns = [
    path('djtinderusers/',
         DjTinderList.as_view(), name="djtinderuser-list"),
    path('djtinderusers/<int:pk>',
         DjTinderDetail.as_view(),
         name="djtinderuser-detail"),
    path('proposals/<user_nick>/<current_latitude>/<current_longitude>/',
         ProposalsApiView.as_view(), name='djtinder_proposals'),

]

