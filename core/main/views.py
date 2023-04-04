from django.shortcuts import render
from .models import Prodcut

def index(request):
    
    if request.method == "POST":
    
        change = request.POST.get("id change")
        delete = request.POST.get("id delete")
        
        
        print("Change: ", change)
        print("Delete: ",delete)
        
        if change != None:
            print("asdaaaa")
            new_name = request.POST.get("new_name")
            new_price = request.POST.get("new_price")
            
            prod = Prodcut.objects.get(id = change)
           
            if new_name != "":
                prod.name = new_name
            
            try:
                if new_price != "":
                    prod.price = int(new_price)
            except:
                pass
            prod.save()
            
        
        if delete != None:
            prod = Prodcut.objects.get(id = delete)
            prod.delete()
        
    prod_list = Prodcut.objects.all()
    
    
    return render(request, "main/index.html", context = {
        "prod_list": prod_list
    })
    
# def shop(request):
    
#     if request.method == "POST":
#         new_price = request.POST.get("new_price")
#         form_id = request.PSOT.get("id")
        
#         prod = Product.objects.get(id=form_id)
        
#         try:
#             prod.product_price = int(new_price)
#         except:
#             pass
        
#         prod.save()
#     product_list = Product.objects.all()
    
#     return render(request, "main/shop.html", context = {
#         "product_list": product_list
#     })
