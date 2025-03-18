import requests
import argparse
import json

BASE_URL = "https://swapi.dev/api/"

def get_film_data(film_title):
    response = requests.get(f"{BASE_URL}films/")
    response.raise_for_status()
    films = response.json()['results']
    
    for film in films:
        if film_title.lower() in film['title'].lower():
            return film
    return None

def get_pilot_data(pilot_url):
    response = requests.get(pilot_url)
    response.raise_for_status()
    return response.json()['name']

def get_starships_and_pilots(film_title):
    film_data = get_film_data(film_title)
    if not film_data:
        print(f"Film '{film_title}' not found.")
        return {}

    starship_data = {}
    for starship_url in film_data['starships']:
        starship_response = requests.get(starship_url)
        starship_response.raise_for_status()
        starship = starship_response.json()
        pilots = [get_pilot_data(pilot) for pilot in starship['pilots']]
        starship_data[starship['name']] = pilots

    return starship_data

def main():
    parser = argparse.ArgumentParser(description="Star Wars Starship Scanner")
    parser.add_argument("film", help="Title of the Star Wars film")
    args = parser.parse_args()
    
    data = get_starships_and_pilots(args.film)
    
    output = json.dumps(data, indent=4)
    print(output)

if __name__ == "__main__":
    main()
