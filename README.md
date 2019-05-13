# ytAutomata
Automation for Subscribe on a YouTube Channel

## Setting up the project

You have to provide a few things to get this project up running.

### Chromedriver

First you have to download the [chromedriver](http://chromedriver.chromium.org/downloads) (Select the version according to your Chrome version) and place it on the project's root directory.

### Selenium for Python

Now you have to install the Selenium package. You can do it in a lot of ways, but I recommend you to use a virtual enviroment. ([see here for more details](https://selenium-python.readthedocs.io/installation.html))
After you're in your virtual enviroment install the selenium package from pip.

```
pip install selenium
```

### Create a Config file

And finally you have to create a config.py file to recieve the inputs (google accounts) and the channel URL. The config.py file has to be on a config folder in the project's root.(config/config.py)
On the config.py file you have to create an array of dictionaries for the inputs and a variable with the channel URL (example below)

```
accounts = [
    {
        'email': "email1@email.com",
        'password': "password"
    },
    ...
]

channelURL = "https://www.youtube.com/channel/UCQ45OjLUjfYlsFpOmWORHRA"
```

## Running the project

Now that you've already setting things up. Just run the automata.py file and have fun!

```
python automata.py
```
