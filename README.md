# Instalation

Note: It is required to have postgres installed

### 1.- Download

    git clone git@github.com:rogerwh/pjBiblioteca.github

### 2.- Create Environment

    mkvirtualenv biblioteca  --python=`which python2`

### 3.- Install Dependencies

    pip install -r requirements.txt

### 4.- Create Database

In shell execute:

    sudo -u postgres createdb biblioteca

In postgres shell:

    CREATE USER biblioteca WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE biblioteca to biblioteca;

### 5.- Migrations

    ./manage.py migrate

### 6.- Load Data

    ./manage.py loaddata autor.json