import requests

def get_jokes(count=10):
    url = "https://official-joke-api.appspot.com/jokes/programming/ten"
    try:
        response = requests.get(url)
        response.raise_for_status()
        jokes = response.json()
        
        for i in range(min(count, len(jokes))):
            joke = jokes[i]
            print(f"Joke {i+1}: {joke['setup']}")
            print(f"Answer: {joke['punchline']}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching jokes: {e}")

if __name__ == "__main__":
    get_jokes()