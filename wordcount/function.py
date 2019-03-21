from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return  render(request, "home.html")
def count(requset):
    text = requset.GET['text']
    count1 = len(text)-6
    word_dict = {}
    for word in text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word]+=1

    sort_list = sorted(word_dict.items(),key=lambda w:w[1],reverse= True)

    return render(requset, "count.html",
                  {'count1':count1,
                   'text':text,
                   'word_dict':sort_list})