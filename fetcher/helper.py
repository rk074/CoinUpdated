import requests

# Replace this with your API endpoint
url = 'https://api.example.com/data'

# If the API requires parameters, you can pass them as a dictionary
params = {
    'key1': 'value1',
    'key2': 'value2'
}

# Making a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)
else:
    print(f"Error: {response.status_code}")