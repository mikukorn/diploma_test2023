import requests
from datetime import datetime

from integrations.models import DroneCIListResults
from integrations.serializers import DroneCIResultsSerializer


DRONE_SERVER = "https://ci.idwell.tech"
DRONE_TOKEN = "aV3DIZvnUUaBmvpiK5PNuu9zTL7fWtvp"


def update_runs():
    endpoint = f'{DRONE_SERVER}/api/repos/iDWELL/idwell-ui-tests/builds'
    headers = {"Authorization": "Bearer aV3DIZvnUUaBmvpiK5PNuu9zTL7fWtvp"}
    response = requests.get(endpoint, headers=headers).json()

    for r in response:
        number_build = r["number"]
        status_build = r["status"]
        autor_build  = r["author_login"]
        date_run     = datetime.utcfromtimestamp(r['finished']).strftime('%Y-%m-%d %H:%M')
        data = {'number': number_build, 'status': status_build, 'autor_build': autor_build, 'date_run': date_run}

        serializer = DroneCIResultsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return "HTTP_201_CREATED"
        return f'HTTP_400_BAD_REQUEST: {serializer.errors}'


def get_build(build_number):
    pass
