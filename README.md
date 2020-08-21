# chit-chat-room
A real-time chat application in Flask.

## How to deploy ?

Get the code
```bash
$ git clone https://github.com/bhu800/chit-chat-room.git
$ cd GCSBot
```
Virtualenv modules installation (Unix based systems)
```bash
$ virtualenv env
$ source env/bin/activate
```
Virtualenv modules installation (Windows based systems)
```bash
$ virtualenv env
$ source env/bin/activate
```

Install modules
```bash
$ pip3 install -r requirements.txt
```   
The chatbot uses heroku-postgresql database for registering users.  So you can make your own app and database in heroku and use that in app. For more info about how to use heroku-postgresql outside of heroku please refer [official documentation.](https://devcenter.heroku.com/articles/connecting-to-heroku-postgres-databases-from-outside-of-heroku)

 After setting up your database, start the application (development mode)
 ```bash
 $ python server.py # default port 5000
 ```
 
 Access the web app in browser: http://127.0.0.1:5000

## What's next ?
- [x] Build a basic chat application with pre-existing different rooms.
- [x] **Bad word filtering**
- [ ] Custom Bad word filtering and warning and user removing feature on consistent use of bad words
- [ ] 'Add Room' functionality 
- [ ] show all online users
- [ ] emojis and stickers for chat
- [ ] Joining multiple rooms at a time
- [ ] Add, Update and View Profile (Profile Image, About) (basicaly a little 'social' touch :D)
- [ ] Different background-image for different lounge
- [ ] Admin Backend, so that some sort of events and discussions can be hosted on the platform
