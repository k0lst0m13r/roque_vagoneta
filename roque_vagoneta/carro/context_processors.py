def importe_total(request):
    total = 410
    """
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + (float(value["precio"]) * value["cantidad"]) """

    return {"importe_total": total}
