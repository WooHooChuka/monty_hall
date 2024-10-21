import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_keep_choice():
    client = APIClient()
    response = client.post(reverse('play_game'), {"choose_option": "keep", "attempts": 100000}, format='json')
    data = response.json()
    wins, losses = data["wins"], data["losses"]
    total = wins + losses
    win_percentage = wins / total * 100
    assert 32 <= win_percentage <= 34

@pytest.mark.django_db
def test_change_choice():
    client = APIClient()
    response = client.post(reverse('play_game'), {"choose_option": "change", "attempts": 100000}, format='json')
    data = response.json()
    wins = data["wins"]
    losses = data["losses"]
    total = wins + losses
    win_percentage = wins / total * 100
    assert 65 <= win_percentage <= 67

