### Dependencies
pythin 3.8 or above

pip install virtualenv

### To run the script
virtualenv .venv 

.venv\Scripts\activate.bat

pip install -r requirements.txt

### Execute test
cd scripts/

py.test

### API Smaples
Sample API's to be used: From https://reqres.in/
https://reqres.in/api/users?page=2  = 200 = GET = User's LIST
https://reqres.in/api/users/2 = 200 = GET = Single User
https://reqres.in/api/users/23 = 404 = GET = User not found
https://reqres.in/api/users = 201 = POST = Body: { "name": "morpheus", "job": "leader"}
https://reqres.in/api/users/2 = 200 = PUT = Request{ "name": "morpheus", "job": "zion resident" }
https://reqres.in/api/users/2 = 200 = PATCH = Request{ "name": "morpheus", "job": "zion resident" }
https://reqres.in/api/users/2 = 204 = DELETE

https://reqres.in/api/register = 200 = POST = Body: {"email": "eve.holt@reqres.in", "password": "pistol" }
https://reqres.in/api/login = 200 = POST = Body: {"email": "eve.holt@reqres.in", "password": "pistol" }
