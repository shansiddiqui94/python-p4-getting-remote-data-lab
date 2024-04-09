import requests
import json

class GetRequester:

    def __init__(self, url):  #Setting the variables for the API linl 
        self.url = url

    def get_response_body(self):           # In this method I am getting back the raw JSON data
        response = requests.get(self.url)
        return response.content             #returning the raw JSON data


    def load_json(self):
        response_content = self.get_response_body() # calling my previous method to get the raw data 
        json_data = json.loads(response_content) #converting the raw data into a python list or dict
        return json_data #returning the new Python converted data

        