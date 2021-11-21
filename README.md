

## Eksi Seyler Crawler


### About The Project


Eksi Seyler is a sub-project of Eksi Sozluk, which contains popular entries written by the users about various categories such as Culture, Science, News, etc. 

This project aims to scrape the contents of the Eksi Seyler for **research purposes**. 

The spider travels between the pages of Eksi Seyler and visits the found URLs. The crawler extracts the title, nick, entry id, entry text, category, date, reading statistics, and sharing statistics. The extracted contents are saved into an SQLite database file.



### Getting Started

### Installation

Before installing the required libraries, It is recommended to create a virtual environment.

The libraries required for the project are listed in the **requirements.txt** file. To download and install the necessary libraries,
```sh
pip install -r requirements.txt
```


### Usage

To start crawling, use
```sh
scrapy crawl entry_spider
```
Extracted contents will be saved into an sqlite database file named **db.sqlite**.

Since crawling might take time, It is recommended to start crawling by using
   ```sh
   scrapy crawl entry_spider -s JOBDIR=crawls/entry_spider-1
   ```
   This command will save the current state of your task when you stop the task by pressing the Ctrl-C or sending a signal. You can resume it later by issuing the same command.
