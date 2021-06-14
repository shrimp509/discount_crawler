# PcHomeDiscountCrawler
For finding out discount price and notify user

## Installation
1. Download `chromedriver` from: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
2. Put `chromedriver.exe` in the same directory of this crawler source code
3. Create python virtual environment:
  ```bash
  $ pip install virtualenv
  $ python -m virtualenv crawler_env
  ```
4. Activate virtual environment and Install related libraries
  ```bash
  $ source crawler_env/bin/activate
  (crawler_env) $ pip install bs4 requests selenium
  (crawler_env) $ deactivate
  ```

## Usage
```bash
$ source crawler_env/bin/activate
$ python pc_home_discount_crawler.rb
```

## Screenshots
