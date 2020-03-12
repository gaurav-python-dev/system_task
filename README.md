[Important note : Since I am using django-debug-toolbar in development setting, each time You redirect on a url on browser, You will get 302 Error from django-debug-toolbar with next redirect link. just click on shown link, and it will redirect to next page. If you don't want this behaviour of redirection, simply comment line no. 6 and 7 in settings\development.py] <br><br>
[Note : I'm using Python 3.7.3 in this project]  <br>

create virtual environment and install all the requirements from requirements.txt
--------------------------------------------------------------------------------
pip install -r reuirement.txt

mention the USER and PASSWORD for DATABASE accordingly in settings\development.py file

create following databases in postgres: 
------------------------------------------
account_detail <br>
database1 <br>
database2 <br>

create following databases in mysql :
----------------------------------------
database3 <br>
database4 <br>
database5 <br>

run the following commands to migrate model into DB:
---------------------------------------------------
python manage.py migrate accounts <br>
python manage.py migrate products --database=database1 <br>
python manage.py migrate products --database=database2 <br>
python manage.py migrate products --database=database3 <br>
python manage.py migrate products --database=database4 <br>
python manage.py migrate products --database=database5 <br>

run the following command to migrate session properly into DB
-------------------------------------------------------------
python manage.py migrate --fake sessions zero <br>
<!-- #below command will show the migration file used to migrate session app -->
python manage.py showmigrations  <br>
python manage.py migrate --fake-initial <br>

create djangoadmin using below command
---------------------------------------
python manage.py createsuperuser<br>
python manage.py runserver<br>
go to http://localhost:8000/admin<br>

add following into Database Model using admin-interface
--------------------------------------------------------
database1 <br>
database2 <br>
database3 <br>
database4 <br>
database5 <br>

Add users into User model and assign them Database and add other details for user <br>

now go to base url : http://localhost:8000 <br>
login as a user and perform the CRUD operation <br>

check the entries in associated DB

