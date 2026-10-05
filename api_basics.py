import json
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print(f"Post ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Content: {data['body']}")

    with open("api_response.json", "w") as file:
        json.dump(data, file, indent=4)

except requests.RequestException as error:
    print(f"API request failed: {error}")