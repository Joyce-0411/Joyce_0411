month=input("enter the month")
date=int(input("enter the date"))
if month in ("jan","feb","mar"):
    print("Summer season")
elif month in ("april","may","june"):
    print("spring season")
elif month in ("july","aug","sep"):
    print("autumn season")
else:
    print("winter season")
if (month=="mar")and (date>20):
    print("summer season")
elif (month=="june") and (date>21):
    print("spring season")
elif (month=="sep") and (date>22):
    print("autumn season")
elif (month=="december")and (date>21):
    print("winter season")
