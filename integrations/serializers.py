from rest_framework import serializers
from integrations.models import TestRunResults, DroneCIListResults


class TestRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRunResults
        fields = ('body_test',)

class DroneCIResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneCIListResults
        fields = ('number', 'status', 'autor_build', 'date_run',)

