import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from usermgmt.forms import InstaWorkUserForm, InstaWorkUserUpdateForm
from usermgmt.models import InstaWorkUser


@csrf_exempt
def handle_user(request, user_id=None):
    """
    handles user
    :param request:
    :return:
    """
    if request.method == 'GET':
        if user_id == None or user_id.strip() == '':
            users = [user.to_response() for user in InstaWorkUser.objects.filter()]
            return HttpResponse(json.dumps(users), status=200, content_type='application/json')
        try:
            user = InstaWorkUser.objects.get(id=user_id)
        except:
            return HttpResponse(status=404)
        return HttpResponse(json.dumps(user.to_response())
                            , status=200, content_type='application/json')

    elif request.method == 'POST':
        form = InstaWorkUserForm(data=json.loads(request.body))
        if not form.is_valid():
            return HttpResponse(status=400)
        form.save()
        return HttpResponse(status=201)

    elif request.method == 'PATCH':
        form = InstaWorkUserUpdateForm(data=json.loads(request.body))
        if not form.is_valid():
            return HttpResponse(status=400)

        updated_request_data = {}

        for value in form.cleaned_data:
            if value is not None:
                if form.cleaned_data[value] is not None:
                    updated_request_data[value] = form.cleaned_data[value]

        try:
            user = InstaWorkUser.objects.get(pk=int(user_id))
            for value in updated_request_data:
                setattr(user, value, updated_request_data[value])
                # user[value] = updated_value[value]
            print(user.to_response())
            user.save()
        except Exception as e:
            return HttpResponse(status=404)
        return HttpResponse(json.dumps(updated_request_data), status=204, content_type='application/json')

    elif request.method == 'DELETE':
        if user_id == None or user_id.strip() == "":
            return HttpResponse(status=400)
        try:
            InstaWorkUser.objects.get(id=user_id).delete()
        except:
            return HttpResponse(status=404)
        return HttpResponse(status=204)
    return HttpResponse(status=400)
