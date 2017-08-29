# crypto-scrape
This is crypto-scrape, a simple webscraper designed to get information on various crypto-currencies from popular online forums and imageboards.

## Why?
crypto-scrape is designed as a tool to be used in conjunction with other projects. By harnessing the power of crypto-scrape, one can easily compare mentions and other metrics of popularity between different crypto-currencies.

These metrics are written to a SQLite database (```cryptos.db```) for easy accessibility and manipulation.

## Roadmap
1. More rigorous testing of reddit sourcing 
2. Move on to source from other websites.

Future: sentiment analysis on post and comment text...

## Configuration
Each source has its own folder within the sources directory. Inside each source's folder are three text files: ```info.txt```, ```included.txt ```, and ```cryptos.txt``` with ```info.txt ``` holding information on setting up that particular source.

Additionally, you must set up an app [here](https://www.reddit.com/prefs/apps/) and enter all relevant information into the ```praw.ini``` file before scraping.

## Usage
As of right now, this project is not incredibly user-friendly. **You must be running Python > v2.5 and have [PRAW](http://praw.readthedocs.io/en/latest/getting_started/installation.html) installed in order for this to run properly.** Note that you may want to change the ```postLimit``` variable within that file before use.

To run:

```
git clone https://github.com/bdscharf/crypto-scrape.git

cd crypto-scrape

python run.py
```

## Applications
Applications of crypto-scrape will be linked here.


