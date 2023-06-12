import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models  import *
from .forms import *

# Create your views here.

import requests
from django.shortcuts import render



def chat_gpt(request):
   
    api_key = ''
   
    # Texto para ser processado pelo modelo GPT-3.5
    prompt =  request.POST['prompt']
   

    # Parâmetros da solicitação para a API do ChatGPT
    payload = {
        'model': 'gpt-3.5-turbo',
        "messages": [{"role": "user", "content": prompt}],
        'temperature': 0.7,
        'max_tokens': 300,
        'stop': ''
    }

    # Faz a solicitação à API do ChatGPT
    headers = {'Authorization': f'Bearer {api_key}'}
    
    response = requests.post('https://api.openai.com/v1/chat/completions', json=payload, headers=headers)
    
    # Extrai a resposta relevante da API
    result = response.json()["choices"][0]["message"]

    # Retorna a resposta obtida pelo chat GPT
    return (result)


def prompt_input(request):
    
     
     if (request.method == 'POST'):
         result=chat_gpt(request)
         
          
     if (request.method == 'GET'):
         return render(request, 'cardap_io/inputGpt.html')
     else: 
         return render(request, 'cardap_io/chatGpt.html',{'result': result})     
     
    



