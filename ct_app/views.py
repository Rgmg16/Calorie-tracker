from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm

def home(request):
    return render(request, 'home.html')

def food_list(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()

    foods = FoodItem.objects.all()
    total_calories = sum(food.calories for food in foods)

    return render(request, 'food_list.html', {
        'form': form,
        'foods': foods,
        'total_calories': total_calories
    })

def delete_food(request, food_id):
    FoodItem.objects.get(id=food_id).delete()
    return redirect('food_list')

def reset_calories(request):
    FoodItem.objects.all().delete()
    return redirect('food_list')

