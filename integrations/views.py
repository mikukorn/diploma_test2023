import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from integrations.serializers import TestRunSerializer, DroneCIResultsSerializer


@api_view(['GET'])
def healthcheck(request):
    if request.method == 'GET':
        return Response("Connection successful", status=status.HTTP_200_OK)
    return Response(status=status.is_server_error)



@api_view(['POST'])
def list_results(request):
    if request.method == 'POST':
        result = {'body_test': request.data}
        serializer = TestRunSerializer(data=result)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def droneci_list_results(request):
#     if request.method == 'GET':
#         result = {'drone_results': request.data}
#         serializer = DroneCIResultsSerializer(data=result)
#         if serializer.is_valid():
#             DroneCIListResults.objects.all().delete()
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     if request.method == 'GET':
#         test_runs = DroneResultModel.objects.all()
#         serializer = DroneSerializer(test_runs, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = DroneSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def list_results(request):
#     if request.method == 'POST':
#         for d in request.data["results"]:
#             serializer = DroneSerializer(data=json.loads(d))
#             if serializer.is_valid():
#                 serializer.save()
#         return Response(serializer.errors, status=status.HTTP_201_CREATED)
#         raise Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




