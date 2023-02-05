import json
from django.core import serializers

from integrations.models import TestRunResults


serialized_data = serializers.serialize('json', TestRunResults.objects.all(), fields=('body_test'))
data = json.loads(serialized_data)
data[0]["fields"]["body_test"]

