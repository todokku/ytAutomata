# ytAutomata
Automation for Subscribe on a YouTube Channel

## Setting up the project

You have to provide a few things to get this project up running.

### Chromedriver

First you have to download the [chromedriver](http://chromedriver.chromium.org/downloads) (Select the version according to your Chrome version) and place it on the project's root directory.

### Depedencies

All the depedencies are on the requirements.txt file. Just intall them with pip

```
pip install -r requirements.txt
```

## Running the project

This is a Flask project and everything is configured to work. Just run the Flask app.

```
flask run
```

## Using the automation

Now the project should be runing on the 5000 port. You have to do a POST request to **localhost:5000/automata** with the following body:

```
{
    "accounts": [
	{
	    "email": "email@email.com",
	    "password": "password"
	},
	{
	    "email": "email2@email.com",
	    "password": "password"
	}
    ],
    "channelURL": "https://www.youtube.com/channel/UCQ45OjLUjfYlsFpOmWORHRA"
}
```

The response should be something like this:

```
{
    "response": [
        {
            "account": "email@email.com",
            "motive": "Already subscribed",
            "subscribed": false
        },
        {
            "account": "email2@email.com",
            "subscribed": true
        }
    ],
    "status": 200
}
```
