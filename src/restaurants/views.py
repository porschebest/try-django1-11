import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based views
# def home_old(request):
#     html_var = 'f string'
#     num = random.randint(0, 10000)
#     html_ = f"""<!DOCTYPE html>
#     <html lang=en>
#         <head></head>
#         <body>
#             <h1>Hello World!</h1>
#             <p>This is {html_var}</p>
#             <p>This is random number {num}</p>
#         </body>
#     </html>
#     """
#     #f string
#     return HttpResponse(html_)

def home(request):
    num = random.randint(0, 10000)
    return render(request, "base.html", {"html_var" : "context variable", "num": num})
