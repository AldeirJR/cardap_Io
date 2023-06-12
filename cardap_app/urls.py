from django.urls import path
from . import views


urlpatterns = [
    path('',views.prompt_input,name="chatInput"),
    path('chatGpt',views.chat_gpt,name="chatReponse"),
    

]
