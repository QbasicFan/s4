# s4
Simple template 4
Template starter

3 Sections + contact

editable Model


Front => auto slider 

Section1s

Section2s




![alt text](https://github.com/QbasicFan/s4/blob/master/ss4.png)



*****************
Install
*****************

1)

git clone https://github.com/QbasicFan/s4 

2) settings.py

INSTALLED_APPS = (
    "s4",
    
    ...
3) settings.py

 os.path.join(PROJECT_ROOT, "[full path to ]/s4/templates"),

4) urls.py

  url("^$", include("s1.urls")),
  
5)
python manage.py makemigrations s4
python manage.py migrate s4

6) re-runserver

***************
SEO/SEM moduleS  


*****************
If you like this starter theme, want help with your django projects or want more advanced django templates visit my website. http://www.philserme.com/

