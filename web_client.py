import requests

def get_posts(url):
  """Makes a GET request and displays post titles."""
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()
    for post in data:
      print(f"Title: {post['title']}")
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

def create_post(url, data):
  """Makes a POST request and displays success message."""
  try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print("Post created successfully!")
    print(f"Response: {response.json()}")
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Step 1: GET request
get_posts("https://jsonplaceholder.typicode.com/posts")

# Step 2: POST request
data = {"title": "Test Post", "body": "This is a test post body", "userId": 1}
create_post("https://jsonplaceholder.typicode.com/posts", data)

# Step 3: Error handling (example)
try:
  requests.get("https://invalidurl.com")  # Replace with a bad URL
except requests.exceptions.RequestException as e:
  print(f"Error: Could not connect to server. {e}")