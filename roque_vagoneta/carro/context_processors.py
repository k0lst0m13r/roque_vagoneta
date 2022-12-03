def importe_total(request):
    total = 0
    
    if request.user.is_authenticated:
         for key, value in request.session["carro"].items():
            total = total + float(value["precio"])
    else:
        total =  "Iniciá sesión para hacer tu pedido"

    return {"importe_total": total}
