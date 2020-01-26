# twitter_api_bot

I wrote this twitter bot as a learing excercise to start to familiarise myself a little more with Python. 

## Features
- Takes a seach term and finds tweets based on it
- Follow user **follow=True** by default,  can be set to false in the code
- Retweet the tweet **retweet=True** by default and **min_num_to_retweet=20**

Retweet and follow options can currently only be turned off in the code. Later plan to enable args from the command line 

## Setup
1. Clone the repo and cd into it
```
git clone git@github.com:NickCallaghan/twitter_api_bot.git
```
2. Set up a virtual environment
 ```
python3 -m venv env
```
3. Activate the virtual environment
```
source env/bin/activate
```
4. Install dependencies
```
pip install requirements.txt
``` 
5. Get you own api key from [Twitter Developers](https://developer.twitter.com/)
6. Create a **keys.py** file in the root of the project and add the following keys:
```
api_key = "ADD_YOUR_KEY_HERE"
api_secret = "ADD_YOUR_KEY_HERE"
access_token = "ADD_YOUR_KEY_HERE"
access_token_secret = "ADD_YOUR_KEY_HERE"
```

