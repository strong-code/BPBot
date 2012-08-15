#BPBot - A helpful IRC robot on Rizon's #fit channel
====================================================

##What is it?
=============
BPBot is an IRC bot written in Python mainly as a learning exercise. It is mainly for
usage in Rizon's #fit channel, but many of the modules it contains are not fitness-specific

##How do I use it?
==================
* Download the repo
* Open config.py and fill in the necessary values
	* Set SSL boolean to 'True' and change the port accordingly if you wish to use an SSL connection

Enter a valid server address
```server = 'server address'```


Enter your desired channel name (multiple channel support coming soon...)
```chan = '#channel name'```


Enter your port number (ensure you have a valid SSL port if SSL is True!)
```port = [port number]```


Enter the nickname you wish BPBot to take
```nick = 'Nickname'```


If have registered the nickname for BPBot on your server, enter the password here
```password = 'password'```


Set SSL to True if you are using an SSL port, otherwise set to False
```SSL = [True/False]```


* Run BPBot.py and enjoy!