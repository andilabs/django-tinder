from django.urls import path
from api.views import (
    ProposalsApiView,
)

urlpatterns = [
    path('proposals/<user_nick>/<current_latitude>/<current_longitude>/',
         ProposalsApiView.as_view(), name='djtinder_proposals'),

]

