#packages are the libraries that we will be using in this project. We will be using the following packages:

"""
numpy: for numerical computations
requests: for making HTTP requests
pandas: for data and spreadsheet manipulation
openai: for using the OpenAI API
beautifulsoup4: to extract data from websites.

"""

#--this can be done by using pip install <package_name> in the terminal. For example, to install numpy, you can use the command: pip install numpy.


#use pip list to see the packages installed in the virtual environment.

import requests

#download a web page
response = requests.get("https://api.github.com")
print(response.status_code) #should print 200 if the request was successful



