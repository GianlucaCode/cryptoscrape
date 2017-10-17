# cryptoscrape
This is cryptoscrape, a simple webscraper designed to get information on various crypto-currencies from popular online forums and imageboards.

## Why?
cryptoscrape is designed as a tool to be used in conjunction with other projects. By harnessing the power of cryptoscrape, one can easily compare mentions and other metrics of popularity between different crypto-currencies.

These metrics are written to a SQLite database (```cryptos.db```) for easy accessibility and manipulation.

## Roadmap
1. More rigorous testing of Reddit sourcing
2. Move on to source from other websites.

## Features
As of right now, cryptoscrape only works with reddit. Read below to see how to configure reddit scraping.

## Configuration
Each source has its own folder within the sources directory. Inside each source's folder are three text files: ```info.txt```, ```included.txt ```, and ```cryptos.txt``` with ```info.txt ``` holding information on setting up that particular source.

Additionally, you must set up an app [here](https://www.reddit.com/prefs/apps/) and enter all relevant information into the ```praw.ini``` file before scraping.

Note: if you are pushing your own version of this project to a Git repository, please ensure that you are **not** pushing your ```praw.ini``` file, as it will contain *your* personal information. See [here](https://stackoverflow.com/questions/3319479/can-i-git-commit-a-file-and-ignore-its-content-changes) for information on ignoring changes to the file, so it will not be uploaded.

## Usage
As of right now, this project is not incredibly user-friendly. **You must be running Python > v2.5 and have [PRAW](http://praw.readthedocs.io/en/latest/getting_started/installation.html)  and [TextBlob](https://textblob.readthedocs.io/en/dev/index.html#get-it-now) installed in order for this to run properly.** This now uses command-line arguments to handle the post limit. See usage below.

To run:

```
git clone https://github.com/bdscharf/cryptoscrape.git

cd cryptoscrape

python run.py [post-limit]
```

## Applications
Applications of crypto-scrape will be linked here.


