from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from apitesting.models import Application
from apitesting.serializers import AppSerializer
from apitesting import configs

@api_view(http_method_names=['GET'])
def all(request):
    apps = Application.objects.all()
    serializer = AppSerializer(apps, many=True)
    return Response({"applications": serializer.data})

@api_view(http_method_names=['POST'])
def test(request):
    api = request.data.get("api")
    app = Application.get(api=api)
    serializer = AppSerializer(app)
    return Response({"application": serializer.data, "api": api})

@api_view(http_method_names=['POST'])
def create(request):
    name = request.data.get("name")
    description = request.data.get("description")
    app = Application.create(name=name, description=description)
    serializer = AppSerializer(app)
    return Response({"application": serializer.data})

@api_view(http_method_names=['POST'])
def update(request):
    api = request.data.get("api")
    app = Application.get(api=api)
    if app is not None:
        updates = request.data.get('updates')
        if updates is not None:
            new_app = app.update(**request.data.get('updates'))
            serializer = AppSerializer(new_app)
            return Response({"application": serializer.data})
        else:
            return Response({"error": '"updates" not found'})
    else:
        return Response({"error": 'application with this "api" not found'})

@api_view(http_method_names=['POST'])
def update_api(request):
    secret_key = request.data.get("secret_key")
    if secret_key == configs.secret_key:
        name = request.data.get("name")
        app = Application.get(name=name)
        if app is not None:
            new_app = app.api_update()
            serializer = AppSerializer(new_app)
            return Response({"application": serializer.data})
        else:
            return Response({"error": 'application with this "name" not found'})
    else:
        return Response({"error": 'secret_key incorrect'})