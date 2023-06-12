# cardap_Io
Aplicativo desenvolvido utilizando Django e React  para consultas a  OpenAI(ChatGPT)
Este é um aplicativo de estudo que utiliza a API do ChatGPT para criar receitas. O aplicativo permite que os usuários façam perguntas sobre receitas e recebam respostas geradas pelo modelo de linguagem do ChatGPT.

Funcionalidades
Os usuários podem digitar uma pergunta relacionada a receitas, por exemplo: "Qual é a receita de panquecas?"
O aplicativo enviará a pergunta para a API do ChatGPT e receberá uma resposta gerada pelo modelo.
A resposta da API será exibida na tela, fornecendo ao usuário informações sobre a receita solicitada.
Requisitos
Python 3.7 ou superior
Biblioteca openai (instalada via pip install openai)
Django (instalado via pip install django)
Configuração
Clone este repositório para o seu ambiente local.
Crie uma conta na OpenAI e obtenha uma chave de API para a API do ChatGPT.
Abra o arquivo settings.py no diretório chatgpt_recipe_app e insira sua chave de API no campo API_KEY.
Execute o servidor Django utilizando o comando python manage.py runserver.
Acesse o aplicativo em seu navegador através do endereço http://localhost:8000.
