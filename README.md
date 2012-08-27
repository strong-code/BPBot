#BPBot - A helpful IRC robot on Rizon's #fit channel
====================================================

##What is it?
=============
BPBot is an IRC bot written in Python mainly as a learning exercise. It is mainly for
usage in Rizon's #fit channel, but many of the modules it contains are not fitness-specific

##How do I use it?
==================
* Download the repo
* Create config.py in the main directory (BPbot/config.py) and fill in the necessary values below
	* Set SSL boolean to 'True' and change the port accordingly if you wish to use an SSL connection
	* Set logging boolean to 'True' if you wish to use logging/quote functionality
	* Enter the IRC Nicknames (not entire username) for people you wish to grant administrative access for BPBot (aka allow quit command)

```python
server = 'server.address.here'
chan = '#ChannelName'
port = [port number]
nick = 'Nickname'
password = 'password'
SSL = [True/False]
logging = [True/False]
admins = ['Me', 'Myself', 'I']
```

* Run BPBot.py and enjoy!