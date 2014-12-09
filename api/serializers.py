from rest_framework import serializers

from models import FuckFinderUser

from django.contrib.gis.geos import fromstr
SEX_CHOICES = (
    ('F', 'Female',),
    ('M', 'Male',),
)



class FuckFinderUserListSerializer(serializers.ModelSerializer):
    # sex = serializers.BooleanField(required=False)
    prefered_sex = serializers.ChoiceField(choices=SEX_CHOICES, default='male')

    class Meta:
        model = FuckFinderUser
        exclude = ('sex',)

    def to_representation(self, instance):
        ret = super(FuckFinderUserListSerializer, self).to_representation(instance)
        pnt = fromstr(ret['last_location'])
        ret['last_location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        return ret