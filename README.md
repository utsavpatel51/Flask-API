# Flask-API
First I create API using Flask.This is just simple user registration api
You can use Postman to send a request on this api
<br/>
1)Run app.py<br/>
2)Send post request from Postman.
    request may look like this<br/>
    <ul>
    <li>URL: http://localhost:5000/register</li>
    <li>Content-Type:application/json</li>
    <li>Raw-Body: 
        {
            "username":"kira",
            "password":"kira"
        }</li></ul>

Also I used this local API into javascript</br>
In request.html file I used XMLHttpRequest to send post request on my api
