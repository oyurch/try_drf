import pytest
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from snippets.models import Snippet
from snippets.views import SnippetViewSet
from django.contrib.auth.models import User

factory = APIRequestFactory()

@pytest.mark.django_db
def test_list():
    view = SnippetViewSet.as_view({'get': 'list'})
    request = factory.get('/snippets/')
    response = view(request)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create():
    user = User.objects.create_user(username='test', password='test')
    view = SnippetViewSet.as_view({'post': 'create'})
    request = factory.post('/snippets/', {'title': 'Test', 'code': 'print("Hello, World!")', 'linenos': False, 'language': 'python', 'style': 'friendly'})
    force_authenticate(request, user)
    response = view(request)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_highlight():
    user = User.objects.create_user(username='test', password='test')
    snippet = Snippet.objects.create(title='Test', code='print("Hello, World!")', linenos=False, language='python', style='friendly', owner=user)
    view = SnippetViewSet.as_view({'get': 'highlight'})
    request = factory.get(f'/snippets/{snippet.pk}/highlight/')
    force_authenticate(request, user)
    response = view(request, pk=snippet.pk)
    assert response.status_code == status.HTTP_200_OK
