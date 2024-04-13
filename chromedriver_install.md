
[Install Chrome Browser](https://skolo.online/documents/webscrapping/#step-2-install-chromedriver)
[Chrome for Testing (Check for latest version)](https://googlechromelabs.github.io/chrome-for-testing/)


Install chromedriver:

```shell
# for ubuntu
# wget https://chromedriver.storage.googleapis.com/{version}/chromedriver_linux64.zip
wget https://chromedriver.storage.googleapis.com/123.0.6312.122/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo mv chromedriver-linux64 /usr/bin/chromedriver-linux64

sudo chown root:root /usr/bin/chromedriver-linux64
sudo chmod +x /usr/bin/chromedriver-linux64
```


Then get in python:

```python
chrome_driver_path = '/usr/bin/chromedriver-linux64/chromedriver'
self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
```
