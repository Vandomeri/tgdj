from django.urls import re_path, include
from django.conf import settings

from .views import (
    start,
    quizes,
    quiz1,
)


urlpatterns = [
    re_path("start", start, name="start"),
    re_path("main_menu", start, name="start"),
    re_path("quizes_list", quizes, name="quizes_list"),
    re_path("quiz1", quiz1, name="quiz1"),
]
