from django.shortcuts import render
from .ml_model import predict_laptop_price


def laptop_price_predict(request):

    result = None

    if request.method == "POST":

        ram = int(request.POST.get("RAM"))
        brand = request.POST.get("Brand")
        processor = request.POST.get("Processor")
        storage = int(request.POST.get("Storage"))

        result = predict_laptop_price(
            ram,
            brand,
            processor,
            storage
        )

    return render(
        request,
        "laptopPrice.html",
        {
            "result": result
        }
    )