from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    if h>=0 and h<12:
        wish="Good Morning"
    elif h>=12 and h<16:
        wish="Good Afternoon"
    else:
        wish="Good Evening"
    my_dict={"date":date,"wish":wish}
    return render(request,"sam.html",my_dict)
