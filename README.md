employees_project
=======

## Installation

For initial project installation of the project for the sake of development,

1. clone the project via

```bash
git clone https://github.com/Avin-Techv/rooftop.git
```

2. create a new git branch with the new functionality name

```bash
git checkout -b feature-fontend_or_backend/feature_name
```

3. comment out the files (this is done beacuse,the project needs csv data for calculations,
and if we run the project without these data,it will show error)

     3.1. rooftop/address/calculations/Calculate.py - Fully

     3.2. rooftop/address/views.py - Fully

     3.3. rooftop/address/urls.py - Excludeing
          line 1 : from rest_framework.routers import DefaultRouter
          line 6 : router = DefaultRouter()

4. run the project
The project can be run in two different ways

     4.1. tradional development run: in traditional development run we the project in two terminals,one with backend and the other with the frontend, first we run the backend part, followed by the frontend part

          backend
          4.1.1. create a python virtual environment

          4.1.2. install all the requirements

          4.1.3. create the postgres database via pgadmin/postgres terminal

          4.1.4. perform migratations

          4.1.5. run django server

          frontend
          4.1.6. got to folder rooftop/frontend

          4.1.7. install packages via

          npm i

          4.1.8. run the frontend

          npm start

     4.2 running via docker

          4.2.1. go to the folder rooftop/

          4.2.2. type and execute the command
          - sudo docker-compose -f docker-compose-dev.yml build

          4.2.3. after successful build type and execute the command
          - sudo docker-compose -f docker-compose-dev.yml up

5. create a django backend superuser

     5.1. create a django superuser via trational way by activateing the environment and in the folder of manage.py file execute

     python manage.py createsuperuser

     5.2. got inside backend docker container create superuser

          5.2.1. make sure docker is running and in a new terminal execute

          sudo docker ps

          5.2.2. in the running services listed find the backend docker container_id and execute

          sudo docker exec -it container_id sh

          5.2.3. go to the folder of manage.py file and execute the following command and give details when prompted

          python manage.py createsuperuser

6. import the csv's

     6.1. login to the django admin panel via superuser credentials

     6.2. in the models if there is an import option present import the csv file with the similar name in the folder rooftop/rooftop/address/sample-csv import that file. For zip codes the main file is too large so we upload it via 3 files by their number 1,2,3

7. uncomment the files

     rooftop/address/calculations/Calculate.py

     rooftop/address/views.py

     rooftop/address/urls.py

8. run again locally via trational way or docker
