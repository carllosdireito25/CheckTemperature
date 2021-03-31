###COMO FAZER O PROJETO RODAR:

##PRIMEIRAMENTE
no terminar instalar as bibliotecas necessarias:\
para o django rodar.
**pip install -r requirements.txt.**

#1° passo:
> primeiramente é necessario criar uma conexao com o banco de dados postgres.
> Uma vez estabelecido a conexão, 
> é necessario criar as seguintes variaveis de ambientes 
> no windows para não expor dados sensiveis.

#2° passo:
As variaveis de ambiente são:

**django_secret_key**,\
**postgres_db_name**,\
**postgres_db_user**,\
**postgres_db_pw**,\
**postgres_host**,\
**postgres_port**,\
**key_openweather**,\
**main_url_openweather**

### OBS:
dê um print() nas variaveis de ambiente criadas para se 
certificar que estao sendo pegas. Caso negativo, reinicie a maquina. 
Nem sempre é reconhecido no exato momento.
A chave da variavel **django_secret_key** será passada por email.
Para a chave **key_openweather** ela é emitida gratuitamente no site
da openweather. Basta gerar uma:

##3° passo:
no terminal, rode o seguinte comando:
> **python manage.py makemigrations**. Com isso , ele fará a migração do 
> modelo criado por mim e dos outros que ainda nao foram.
> Feito isso, rode o comando: **python manage.py migrate**

##4° passo:
Faça um check no banco de dados e em tabelas voce verá
que foi criado uma tabela chamada "core_weatherrecords".
o **"CORE"** é porque por padrao o django coloca o nome da aplição
(no meu caso chamada de CORE) na frente.

##5° passo:
no terminal, execute o comando:
**python manage.py runserver.**

##6 passo:
Ao executar o passo 5, no terminal ira aparecer uma URL. 
clique para poder navegar.


#CONSIDERACOES FINAIS:
A) O projeto foi feito em django pois acho mais prático\
a integracao do backend com o frontend. Alem disso,\
a ORM já é integrada com o django. De toda forma,\
eu poderia ter feito com flask + sqlAlchemy ou com Fastapi.\

b)A aplicação é bem simples, em especial o frontend.\
não houve tratativa dos parametros ou algo do tipo.\
A ideia é justamente mostrar como o django funciona.
Na web, é possivel digitar alguma cidade\
e ela devolve a temperatura.\
e é possivel pesquisar quantas vezes foi feita pesquisa\
para aquela cidade em especifico,\ 
inclusive incluindo o horario da busca.





