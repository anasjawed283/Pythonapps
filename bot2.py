import requests

def get_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # URL to visit
    target_url = "url"

    # Number of iterations
    num_iterations = 1000

    for _ in range(num_iterations):
        website_content = get_website_content(target_url)

        if website_content:
            print("Successfully retrieved website content:")
            print(website_content[:500])  # Print the first 500 characters as an example
        else:
            print("Failed to retrieve website content.")
