# BenzingaScrape

![GitHub license](https://img.shields.io/github/license/ahmedemad2002/BenzingaScrape)
![GitHub stars](https://img.shields.io/github/stars/ahmedemad2002/BenzingaScrape)
![GitHub forks](https://img.shields.io/github/forks/ahmedemad2002/BenzingaScrape)
![GitHub issues](https://img.shields.io/github/issues/ahmedemad2002/BenzingaScrape)

## Description

BenzingaScrape is a Python script that allows you to scrape data from the [Benzinga Dividend Calendar](https://www.benzinga.com/calendars/dividends) page. It provides a convenient way to extract the data from the table shown on the page.
It sends the request to the API directly instead of using web browser agent like Selenium webdriver.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Sample Output](#sample-output)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python (version X.X.X)
- httpx
- pandas
- os

## Getting Started

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/YourUsername/BenzingaScrape.git

### Usage

1. Navigate to the project directory:
   ```sh
   cd BenzingaScrape
2. Run the scraping script:
    python scraping_script.py
The scraped data will be organized into data frames using the pandas library, and the resulting data frames will be saved in the "output" directory. If a file with the same name already exists in the "output" directory the script will append the new data to the existing file and deduplicate the data using pandas library.