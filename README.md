# project-a-22

For local host
Home page: http://localhost:8000 or http://127.0.0.1:8000 (The two are interchangable, but would affect login)
Assignments page: http://localhost:8000/assignment
Assignmnets List page: http://localhost:8000/list

For login I followed this page
https://www.section.io/engineering-education/django-google-oauth/

Settings already has all that's necessary, just need to pip install django-allauth
or install requirements

To connect with personal machine, follow steps 4-5, create new google api, add social app on django admin

http://localhost:8000/accounts/login    - link to login, should redirect to homepage after login, can create new account (with google) or just login with admin
http://localhost:8000/logout    - link to logout

If you want to be able to login with http://localhost:8000, need to add http://localhost:8000 to the google credentials and admin page

