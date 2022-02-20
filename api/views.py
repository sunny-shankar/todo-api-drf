from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.decorators import api_view

from api.serializer import TodoSerializer
from api.models import TodoModel


@api_view(['GET', 'POST'])
def get_all_objects(requests):
    query = TodoModel.objects.all()
    serializer = TodoSerializer(query, many=True)

    if requests.method == "POST":
        serializer = TodoSerializer(data=requests.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def get_object(requests, pk):
    query = TodoModel.objects.get(pk=pk)
    serializer = TodoSerializer(query)
    if requests.method == "DELETE":
        query.delete()
        return Response({"message": "Object Deleted Successfully"})
    if requests.method == "PUT":
        serializer = TodoSerializer(query,data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    return Response(serializer.data)