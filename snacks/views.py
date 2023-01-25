from django.shortcuts import render

def snacks(request):
    return render(request, 'snack_list.html')

def snacksDetail(request):
    return render(request, 'snack_detail.html')
