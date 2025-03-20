from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import Http404

from main.models import Car, Sale


def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    template_name = 'main/list.html'
    context = {'cars': cars}
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    # получите авто, если же его нет, выбросьте ошибку 404
    template_name = 'main/details.html'
    context = {'car': car}
    return render(request, template_name, context)  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        car = get_object_or_404(Car, pk=car_id)  # Получаем автомобиль или 404
        sales = Sale.objects.filter(car=car)  # Получаем продажи для автомобиля
        template_name = 'main/sales.html'
        context = {'car': car, 'sales': sales}  # Передаем данные в шаблон
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')


