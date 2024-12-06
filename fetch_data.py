import os
import requests

def load_env(filename):
    """
    Loads environment variables from a .env file.
    """
    with open(filename) as f:
        for line in f:
            # Ignore comments and empty lines
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value
def fetch_aoc_input(year, day, session_cookie, output_file):
    """
    Fetches the input for a specific Advent of Code day and saves it to a file.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={SESSION_COOKIE}"}
    
    try:
        # Make the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Save to file
        with open(output_file, "w") as file:
            file.write(response.text.strip())
        print(f"Input for Day {day}, {year} saved to {output_file}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching input: {e}")

# Example Usage
if __name__ == "__main__":
    # Load environment variables from the .env file
    load_env(".env")

    # Retrieve values from the environment
    AOC_YEAR = 2024
    AOC_DAY = 7
    SESSION_COOKIE = os.getenv("SESSION_COOKIE")
    OUTPUT_FILE = f"data_{AOC_DAY}.txt"
    
    fetch_aoc_input(AOC_YEAR, AOC_DAY, SESSION_COOKIE, OUTPUT_FILE)

