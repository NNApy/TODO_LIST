from django.conf.urls import url

from todo_list.views import index, add_task, delete, edit, up_down

urlpatterns = [
    url(r'^up_down', up_down, name='up_down'),
    url(r'^edit', edit, name='edit'),
    url(r'^del/', delete, name='del'),
    url(r'^add_task/', add_task, name='add_task'),
    url(r'^$', index, name='index')

]
