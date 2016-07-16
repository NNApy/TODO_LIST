from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Tasks
from django.db.models import Max, Min

def index(request):
    context = {'tasks_data': Tasks.objects.filter().order_by('-position')}
    return render(request, 'todo_list.html', context)


def add_task(request):
    if request.method == "POST":
        if request.POST.get('task_name') == '':
            return HttpResponse('The task can not be empty')
        if request.POST.get('done'):
            done = 1
        else:
            done = 0
        if Tasks.objects.count() == 0:
            position = 1
        else:
            position = int(''.join(Tasks.objects.aggregate(Max('position')).values())) + 1
        Tasks.objects.create(task_name = request.POST.get('task_name').strip(),
                            done = done,
                            position = position)
        return redirect(index)
    else:
        return render(request, 'add_task.html')


def delete(request):
    Tasks.objects.filter(id=request.GET.get('id')).delete()
    return redirect(index)



def edit(request):
    if request.method == 'GET':
        if Tasks.objects.filter(id=request.GET.get('id')):
           context = {'edit_data': Tasks.objects.filter(id=request.GET.get('id')).get()}
           return render(request, 'edit.html', context)
        else:
            return HttpResponse('This task does not exist')
    else:
        if request.POST.get('task_name') == '':
            return HttpResponse('The task can not be empty')
        if request.POST.get('done'):
            done = 1
        else:
            done = 0
        Tasks.objects.filter(id = request.POST.get('id')).update(task_name=request.POST.get('task_name').strip(),
                                                                done=done)
        return redirect(index)


def up_down(request):
    if request.GET.get('action') == u'up':
        if ''.join(Tasks.objects.aggregate(Max('position')).values()) == request.GET.get('position'):
            return redirect(index)
        x = 1
    elif request.GET.get('action') == u'down':
        if ''.join(Tasks.objects.aggregate(Min('position')).values()) == request.GET.get('position'):
            return redirect(index)
        x = -1

    p_list = []
    for dict in Tasks.objects.filter():
        p_list.append(dict.position)

    position_list = sorted(p_list)
    indx_down = position_list.index(request.GET.get('position'))

    our_position = Tasks.objects.filter(position=request.GET.get('position')).get()
    our_position_id = our_position.id

    next_position = sorted(position_list)[indx_down + x]
    next_line_down = Tasks.objects.filter(position=next_position).get()
    next_position_id = next_line_down.id

    Tasks.objects.filter(position=request.GET.get('position'), id=our_position_id).update(position=next_position)
    Tasks.objects.filter(position=next_position, id=next_position_id).update(position=request.GET.get('position'))
    return redirect(index)

