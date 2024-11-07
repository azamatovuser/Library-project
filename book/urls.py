from django.urls import path
from book.views import index, detail, create, update, delete, download_counter


urlpatterns = [
    path("", index, name='index'),
    path("detail/<int:pk>/", detail, name='detail'),
    path("create/", create, name='create'),
    path("update/<int:pk>/", update, name='update'),
    path("delete/<int:pk>/", delete, name='delete'),
    path("download/<int:pk>/", download_counter, name='download'),
]