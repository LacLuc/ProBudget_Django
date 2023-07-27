https://fit-tecnologia.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/learn/lecture/29329990#overview
11. Iniciando o primeiro projeto com Django e Venv
17. [PARA ALUNOS AVANÇADOS] - Play
24. Templates e renderização de HTML no Django
27. Adicionando font-awesome no template

python -m venv venv
.\venv\Scripts\Activate
python.exe -m pip install --upgrade pip
pip install pytest
pip install django
django-admin --versin
pip freeze
pytest
django-admin --version
pip install pip setuptools wheel --upgrade
pip install -U mypy
pip install -U flake8

pip install -r requirements.txt
pip freeze > requirements.txt

##Remover pasta
rm -Rf projeto

django-admin serve apenas para Criar
django-admin startproject src .


python manage.py startapp budget

subir o servidor.
python manage.py runserver















django-admin --help
[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver