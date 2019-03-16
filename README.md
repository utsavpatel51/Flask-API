# Flask-API
First I created API using Flask.This is just simple user registration api
You can use Postman to send a request on this api
1)Run app.py 
2)Send post request from Postman 
    request may look like this
    URL: http://localhost:5000/register
    Content-Type:application/json
    Raw-Body: 
        {
            "username":"kira",
            "password":"kira"
        }

Also i used this local pai into javascript
In request.html file I used XMLHttpRequest to send post request on my api