import requests, json

def get_country_info(country):
    '''
    Fetches information about a country from the REST Countries API.
    
    Parameters:
    country (str): The name of the country to fetch information for.
    
    Returns:
    dict: A dictionary containing information about the country, or an error message if the country is not found.
    
    '''

    url = 'https://api.restcountries.com/countries/v5'
    params = {"q": country}
    response = requests.get(url, params=params, headers={'Authorization': 'Bearer REMOVED_API_KEY'})
    if response.status_code != 200:
        print("Error fetching data from API")
        exit()
    elif response.status_code == 200:
        print("Data fetched successfully")
    country_data = response.json()
    print(response.url)
    print(json.dumps(country_data, indent=4))
    if not country_data["data"]["objects"]:
        return {"Error": "Country not found"}
    country_info = country_data["data"]["objects"][0]
    country_dict = {
            "Country Name": country_info["names"]["common"],
            "Official Name": country_info["names"]["official"],
            "Capital": country_info["capitals"][0]["name"],
            "Region": country_info["region"],
            "Population": country_info["population"],
            "Area": country_info["area"]["kilometers"],
            "Currency": country_info["currencies"][0]["name"],
            "Currency Symbol": country_info["currencies"][0]["symbol"],
            "Languages": [language["name"] for language in country_info["languages"]]}
    return country_dict

def display_country_info(country_info):
    print(f'''
        =====================================
                COUNTRY EXPLORER
        =====================================
    ''')
    print(f"Country Name: {country_info['Country Name']}")
    print(f"Official Name: {country_info['Official Name']}")
    print(f"Capital: {country_info['Capital']}")
    print(f"Region: {country_info['Region']}")
    print(f"Population: {country_info['Population']:,.0f}")
    print(f"Area: {country_info['Area']:,.1f} km²")
    print(f"Currency: {country_info['Currency']} ({country_info['Currency Symbol']})")
    print(f"Languages: {', '.join(country_info['Languages'])}")

def compare_countries(country1, country2):
    '''
    Compares two countries based on their population and area.
    
    parameters:
    country1 (str): The name of the first country to compare.
    country2 (str): The name of the second country to compare.
    
    Returns:
    None: Prints the comparison results to the console.
    
    '''

    country1_info = get_country_info(country1)
    country2_info = get_country_info(country2)
    if "Error" in country1_info:
        print(country1_info["Error"])
        return
    if "Error" in country2_info:
        print(country2_info["Error"])
        return
    population1 = country1_info['Population']
    population2 = country2_info['Population']
    area1 = country1_info['Area']
    area2 = country2_info['Area']

    print(f'''
        =====================================
                COUNTRY COMPARISON
        =====================================
    ''')
    print(f"{country1_info['Country Name']} vs {country2_info['Country Name']}")
    print(f"\n{country1_info['Country Name']}")
    print(f"Population: {population1:,.0f}")
    print(f"Area: {area1:,.1f} km²")
    print(f"\n{country2_info['Country Name']}")
    print(f"Population: {population2:,.0f}")
    print(f"Area: {area2:,.1f} km²")

    if population1 > population2:
        print(f"\n{country1_info['Country Name']} has a larger population than {country2_info['Country Name']}.")
    elif population1 < population2:
        print(f"\n{country2_info['Country Name']} has a larger population than {country1_info['Country Name']}.")
    else:
        print(f"\nBoth countries have the same population.")

    if area1 > area2:
        print(f"\n{country1_info['Country Name']} has a larger area than {country2_info['Country Name']}.")
    elif area1 < area2:
        print(f"\n{country2_info['Country Name']} has a larger area than {country1_info['Country Name']}.")
    else:
        print(f"\nBoth countries have the same area.")

def get_african_countries():
    '''
    Fetches a list of African countries from the REST Countries API.
    
    Returns:
    list: A list containing the names of African countries.
    
    '''
    url = 'https://api.restcountries.com/countries/v5'
    params = {"region": "Africa",
              "limit" : 100}
    response = requests.get(url, params=params, headers={'Authorization': 'Bearer REMOVED_API_KEY'})
    if response.status_code != 200:
        print("Error fetching data from API")
        exit()
    african_countries_data = response.json()
    african_countries_list = []
    for country_info in african_countries_data["data"]["objects"]:
        country_name = country_info["names"]["common"]
        african_countries_list.append(country_name)
    return african_countries_list


def main():
    while True:
        print('''
        =====================================
                COUNTRY EXPLORER
        =====================================
        
        1. Get information about a country
        2. Compare two countries
        3. List African countries
        4. List countries by region
        5. Exit

        Choose an option (1-5):
    ''')
        option = input()
        if option == '1':
            country = input("Enter the name of the country: ").lower()
            country_info = get_country_info(country)
            if "Error" in country_info:
                print(country_info["Error"])
            else:
                display_country_info(country_info)
        elif option == '2':
            country1 = input("Enter the name of the first country: ").lower()
            country2 = input("Enter the name of the second country: ").lower()
            compare_countries(country1, country2)
        elif option == '3':
            african_countries = get_african_countries()
            print(f'''
        =====================================
                AFRICAN COUNTRIES
        =====================================
            ''')
            for country in african_countries:
                print(f"{country}")
        elif option == '4':
            pass
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()