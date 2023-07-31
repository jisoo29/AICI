from django.urls import path
from . import views

app_name = "board"
urlpatterns = [
    path("", views.notice, name="notice"),
    path("post/", views.post, name="post"),
    path("content/<int:brd_id>/", views.content, name="content"),
    path("content/<int:brd_id>/edit/", views.edit, name="edit"),
    path("content/<int:brd_id>/delete/", views.board_delete, name="delete"),
    path("board_list/", views.board_list, name="board_list"),
]
