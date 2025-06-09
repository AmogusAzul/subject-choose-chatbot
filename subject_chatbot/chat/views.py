from django.shortcuts import render

def chat_ui_view(request):

    return render(request, 'chat/chat_ui.html')

# Create your views here.
