from django.shortcuts import render
def mileage(request):
    km = int(request.POST.get('Distance', 0))
    lt = int(request.POST.get('fuel', 0))
    mileage = km/lt if request.method == 'POST' else 0
    print("Distance=",km)
    print("fuel=",lt)
    print("mileage=",mileage)
    return render(request, 'mathapp/math.html', {'km': km, 'lt': lt, 'mileage':mileage})
