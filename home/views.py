from django.shortcuts import render, redirect
from django.http import JsonResponse
# from plotly.offline import plot
# import plotly.graph_objs as go

from .logic import mainLogic, graphs

from django.contrib.auth.decorators import login_required

clusterInfo, labels = mainLogic.kmean()

def api(requests):
    dataReq = requests.GET["data"]

    if dataReq == "AgeRange" :
        return JsonResponse(mainLogic.giveAssocOnAgeRange(int(requests.GET["startAge"]),int(requests.GET["endAge"])))

    elif dataReq == "Recomms" :
        return JsonResponse(mainLogic.giveAssocRight(requests.GET["query"]))

    elif dataReq == "Aprs" :
        return JsonResponse(mainLogic.apr(int(requests.GET["cluster"]), float(requests.GET["ms"]), float(requests.GET["mc"]), float(requests.GET["ml"])))

@login_required
def home(requests):
    context = {
        'activeTab' : "dashboard",
        'maxFreq' : graphs.plotMaxFreq(),
        'mVf' : graphs.plotMaleVsFemale(),
        'genderSpending' : graphs.genderVsSpendingPower(),
    }
    return render(requests, 'home/welcome.html', context)

AgeRanges = [
    '18-25',
    '26-33',
    '34-41',
    '42-49',
    '50-57',
    '58-65',
    '66-70'
]
@login_required
def recommendations(request):
    context = {
        'activeTab' : "recommendations",
        'AgeRanges': AgeRanges,
    }
    return render(request, 'home/recommendations.html', context)
@login_required
def clustering(request):
    context = {
        'activeTab' : "clustering",
        'plot' : graphs.plotScatter(clusterInfo, labels)
    }
    return render(request, 'home/clustering.html', context)
@login_required
def aprOnClustering(request):
    context = {
        'activeTab' : "aprOnClustering",
        'clusters' : ['0','1','2','3','4']
    }
    return render(request, 'home/aprOnClustering.html', context)