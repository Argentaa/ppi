
# PPI Flask

Avanço na carreira aos titulares de cargos integrantes do Plano de Carreira e Cargos de Magistério do Ensino Básico, Técnico e Tecnológico que integram os Quadros de Pessoal das Instituições Federais de Ensino




## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .flaskenv

`FLASK_APP = PPI Flask`

`FLASK_DEBUG = 1`

Se você não criar o arquivo com as variáveis de ambiente, você tera que colocar essas variáveis no cmd manualmente, com os seguintes comandos

`set FLASK_APP = PPI Flask`

`set FLASK_DEBUG = 1`

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/Argentaa/ppi.git
```

Instale as dependências

```bash
  pip install flask
  pip instal mysql.connector
  pip install python-dotenv
  pip install flask-login
```

Inicie o servidor

```bash
  flask run
```

