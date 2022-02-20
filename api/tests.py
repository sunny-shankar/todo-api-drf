from django.test import TestCase, Client
from api.models import TodoModel
from api.serializer import TodoSerializer
from rest_framework import status
from rest_framework.test import APITestCase,APIClient

client = APIClient()


class GetAllTodoTest(APITestCase):

    def setUp(self) -> None:
        TodoModel.objects.create(title="Do Some thing", description="Try Doing...")
        TodoModel.objects.create(title="Do #1 thing", description="Try Doing #1...")
        TodoModel.objects.create(title="Do #2 thing", description="Try Doing #2...")
        TodoModel.objects.create(title="Do #3 thing", description="Try Doing #3...")

    def test_get_all_todo_objects(self):
        response = client.get("/api/")
        print(response.data)
        query = TodoModel.objects.all()

        serializer = TodoSerializer(query, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
