function runBot()
{
    var username = document.querySelector('#username').value;
    var password = document.querySelector('#password').value;
    var usernames = document.querySelector('#usernames').value;
    var messages = document.querySelector('#message').value;
    if(username =! '' && password != '' && usernames != '' && messages != ''){
        var username = document.querySelector('#username').value;
        var password = document.querySelector('#password').value;
        var usernames = document.querySelector('#usernames').value;
        var messages = document.querySelector('#message').value;
        document.querySelector('.light').innerHTML = '';
        document.querySelector('.light').classList.add('light2');
        document.querySelector('.light').innerHTML = '<div class="status"><h1>STATUS</h1><h2 id="status">Trying to Login<br>Dont touch Your Keyboard</h2><div class="sr"><div><h4>Message Sent -<h4><h1 id="ms">0</h1></div><div><h4>Errors -<h4><h1 id="me">0</h1></div></div></div>';
        eel.runBot(username,password,usernames,messages);
    }
}

eel.expose(status);
function status(x)
{
    if(x=="Login Not Successfull")
    {
        document.getElementById('status').innerHTML="Login Failed <br> Check your password maybe :p";
    }
    else if(x=="Sending Messages")
    {
        document.getElementById('status').innerHTML="Sending Messages <br>Don't touch Your Keyboard ";
    }
    else if(x=="done")
    {
        document.querySelector('.light').innerHTML=' <div class="status"><h1>STATUS</h1><h2 id="status">Done! <br> Thanks for Using</h2><h1>Contact Me :)</h1><div class="contact"><a href="https://www.linkedin.com/in/rakshit-arora-1470b2163/"><img src="https://img.icons8.com/dusk/60/000000/linkedin.png"/></a><a href="https://www.instagram.com/im.rakshit/"><img src="https://img.icons8.com/dusk/60/000000/instagram-new.png"/></a><a href="https://twitter.com/rakshit087"><img src="https://img.icons8.com/dusk/60/000000/twitter.png"/></a></div></div>'
    }
}

eel.expose(messageStatus);
function messageStatus(x,y)
{
    document.getElementById('ms').innerHTML=x;
    document.getElementById('me').innerHTML=y;
}
