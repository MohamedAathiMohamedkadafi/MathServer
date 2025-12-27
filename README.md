# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```

<html>
<head>
    <title>Fuel Efficency</title>
    <style>
        body {
            background-color: rgb(2, 2, 31);
            
            font-family:century;

            font-size: 40px
}
        
        .box {
            width: 800px;
            margin: auto;
            margin-top: 140px;
            padding: 150px;
            background-color: #ff0048;
            color: rgb(0, 0, 0);
            border: 4px pointer rgb(139, 24, 181);
            text-align: center;
            font-size: 19px
            
            
        }
        input {
            padding: 4px;
            margin: 7px;
            font-size: 10px
        }
        .btn {
            padding: 7px 16px;
            cursor: pointer;
            font-size: 10px
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>Fuel Efficency Calculator </h1>
        <h2>Mohamed Aathil M (25008235)<h2>
        

        <form method="POST">
            {% csrf_token %}
            Distance(km):
            <input type="text" name="Distance" vaclue="{{ km }}"><br>

            fuel consumed(liters):
            <input type="text" name="fuel" value="{{ lt }}"><br>

            <button class="btn" type="submit">Calculate</button><br><br>

            mileage:
            <input type="text" value="{{mileage }}" readonly> km/lt
            
        </form>
    </div>
</body>
</html>
```
```

from django.contrib import admin
from django.urls import path 
from mathapp import views

urlpatterns = [
    path('',views.mileage, name='mileage'),
]
```
```
from django.shortcuts import render
def mileage(request):
    km = int(request.POST.get('Distance', 0))
    lt = int(request.POST.get('fuel', 0))
    mileage = km/lt if request.method == 'POST' else 0
    print("Distance=",km)
    print("fuel=",lt)
    print("mileage=",mileage)
    return render(request, 'mathapp/math.html', {'km': km, 'lt': lt, 'mileage':mileage})

```
## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2025-12-27 125936.png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot 2025-12-27 125634.png>)
## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
