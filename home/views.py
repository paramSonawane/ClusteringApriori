from django.shortcuts import render
from django.http import JsonResponse
# from plotly.offline import plot
# import plotly.graph_objs as go

from .logic import mainLogic, graphs

clusterInfo, labels = mainLogic.kmean()

def api(requests):
    dataReq = requests.GET["data"]

    if dataReq == "AgeRange" :
        return JsonResponse(mainLogic.giveAssocOnAgeRange(int(requests.GET["startAge"]),int(requests.GET["endAge"])))

    elif dataReq == "Recomms" :
        return JsonResponse(mainLogic.giveAssocRight(requests.GET["query"]))

    elif dataReq == "Aprs" :
        return JsonResponse(mainLogic.apr(int(requests.GET["cluster"]), float(requests.GET["ms"]), float(requests.GET["mc"]), float(requests.GET["ml"])))


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

def recommendations(request):
    context = {
        'activeTab' : "recommendations",
        'AgeRanges': AgeRanges,
    }
    return render(request, 'home/recommendations.html', context)

def clustering(request):
    context = {
        'activeTab' : "clustering",
        'plot' : graphs.plotScatter(clusterInfo, labels)
    }
    return render(request, 'home/clustering.html', context)

def aprOnClustering(request):
    context = {
        'activeTab' : "aprOnClustering",
        'clusters' : ['0','1','2','3','4']
    }
    return render(request, 'home/aprOnClustering.html', context)