from django.shortcuts import render
from .models import Verb
from django.core import serializers
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt



def verbs_view(request):
    # create data dictionary
    json_serializer = serializers.get_serializer("json")()

    verbs = Verb.objects.all()
    verbs_json = json_serializer.serialize(Verb.objects.all().order_by('infinitif'), ensure_ascii=False)
    
    context = {
        'verbs': verbs,
        'verbs_json': verbs_json,
    }

    return render(request, "french/verbs.html", context)



@csrf_exempt
def select_verbs_view(request):

    if request.method == 'POST':

        request.session["verb_pks"] = list(request.POST.keys())
        return HttpResponseRedirect('../select_tenses')
    
    # create data dictionary
    json_serializer = serializers.get_serializer("json")()

    verbs = Verb.objects.all().order_by('infinitif')

    verbs_json = json_serializer.serialize(Verb.objects.all().order_by('infinitif'), ensure_ascii=False)
    
    context = {
        'verbs': verbs,
        'verbs_json': verbs_json,
    }

    return render(request, "french/select_verbs.html", context)

@csrf_exempt
def select_tenses_view(request):

    if request.method == 'POST':

        request.session["tenses"] = list(request.POST.keys())
        print(request.session["tenses"])
        return HttpResponseRedirect('../select_POVs')

    return render(request, "french/select_tenses.html")


@csrf_exempt
def select_POVs_view(request):

    if request.method == 'POST':

        request.session["POVs"] = list(request.POST.keys())
        print(request.session["tenses"])
        return HttpResponseRedirect('../practice')

    return render(request, "french/select_POVs.html")



@csrf_exempt
def practice_view(request):

    verbs = Verb.objects.filter(pk__in=request.session["verb_pks"])
    # print(verbs)
    print(request.session["verb_pks"])
    print(request.session["tenses"])
    print(request.session["POVs"])

    context = {
        "verbs": verbs,
    }

    return render(request, "french/practice.html", context)


def random_view(request):

    return render(request, "french/random.html")