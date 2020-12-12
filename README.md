# 🌐 Content Aggregator Website using Django Server

Referring different websites for the latest blogs on a topic is a tedious task. I have developed this content aggregator specifically for machine learning blogs.

> A content aggregator is a system which aggregates latest blogs from the websites and displays them at one place.

## 💻 Steps to Run

  - Clone the project using command ```git clone https://github.com/hardymunjal/Content_Aggregator_Django_Server.git```
    > You can also directly download the zip file and unzip it in the preferred location.
  - Setup python virtual environment:
    - Make a virtual environment using command:
      ```
      virtualenv -p [your python2/python3 path] content_aggregator
      ```
    - Activate the virtual environment using command:
      ```
      source content_aggregator/bin/activate
      ```
    > ***Note: The above commands work for a linux system. Commands may change for windows or Mac.***
  - Make sure you are in directory - ___Content_Aggregator_Django_Server/server/___
  
  - Install the python packages from [requirements file](https://github.com/hardymunjal/Content_Aggregator_Django_Server/blob/main/server/req.txt) using command:
    ```
    pip install -r req.txt
    ```
  - Run the django server using command:
    ```
    python manage.py runserver [ip]:[port]
    ```
  - Visit [ip]:[port] in your browser and you should see the django server running. For example if running on localhost and port 9000, you can type in the browser ```http://localhost:9000```
    > You will get a ****Page not found**** error as no url is maped to path http://localhost:9000/
    
## ✔ Demo

  - Starting django server

    <p align="center">
      <img src="https://github.com/hardymunjal/Content_Aggregator_Django_Server/blob/main/server/static_assets/images/server_start.PNG?raw=true">
    </p>
    
  - Content Aggregator Webpage
    
    <p align="center">
      <img src="https://github.com/hardymunjal/Content_Aggregator_Django_Server/blob/main/server/static_assets/images/webpage_view.PNG?raw=true">
    </p>
    
  - All the mapped URL
  
    <p align="center">
      <img src="https://github.com/hardymunjal/Content_Aggregator_Django_Server/blob/main/server/static_assets/images/urls.PNG?raw=true">
    </p>
    
  - Microsoft Example
    <p align="center">
      <img src="https://github.com/hardymunjal/Content_Aggregator_Django_Server/blob/main/server/static_assets/images/microsoft_example.png?raw=true">
    </p>
    
## 🔗 API Endpoints Explained
  
  - /view/webpage - Displays the content aggregator webpage
  - /scrape/{blog_name}/{count} - Scrapes content from blog whose name is specified and returns the latest blogs as per the number of count specified.
    - blog_name: microsoft or mlm or spectator or fastml
    - count: any positive number
    > Example: /scrape/spectator/10 - Scrapes 10 latest blogs from The Spectator blog.

## 🕷 Scrapers

I have implemented 4 scrapers in the project:
  - [Microsoft’s Machine Learning Blog](https://blogs.technet.microsoft.com/machinelearning/)
  - [Machine Learning Mastery](https://machinelearningmastery.com/about/)
  - [The Spectator](http://blog.shakirm.com/)
  - [FastML](http://fastml.com/)
