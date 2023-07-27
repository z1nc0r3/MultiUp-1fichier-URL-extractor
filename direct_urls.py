import sys
import os
import requests
from bs4 import BeautifulSoup
import re
import time

def extract_direct_urls(action_url, adz):
    payload = {"adz": adz}
    output = open('direct.txt', 'a')
    retrying_text = "Rate limit detected. Retrying in {countdown_seconds} seconds.."
    
    with requests.request("POST", action_url, data=payload) as response:
        if response.status_code == 404:
            print("File not found. Please provide a valid 1fichier URL.")
            return
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Check if the page contains "Please wait ⏳" text
        while "Please wait ⏳" in soup.get_text():
            countdown_seconds = 10
            
            while countdown_seconds > 0:
                sys.stdout.write(f"\r{retrying_text.format(countdown_seconds=countdown_seconds)}")
                sys.stdout.flush()
                time.sleep(1)
                countdown_seconds -= 1
                
            sys.stdout.write("\r" + " " * (len(retrying_text) + 5) + "\r")  # Clear the last message
            sys.stdout.flush()
                
            with requests.request("POST", action_url, data=payload) as response:
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")

        direct_url = soup.find("a", attrs={"class": "ok btn-general btn-orange"})["href"]
        print(direct_url)
        output.write(direct_url + "\n")
        output.flush()


def extract_form_values(url):
    pattern = r"\d+$"
    AF = re.search(pattern, url).group(0)
    headers = {
        'Cookie': f'AF={AF}; show_cm=no'
    }

    response = requests.request("GET", url, headers=headers)
    
    if response.status_code == 404:
        print("File not found. Please provide a valid 1fichier URL.")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
        
    form = soup.find("form", attrs={"class": "alc"})
    input = soup.find("input", attrs={"name": "adz"})
    
    action_url = None
    adz = None

    if form and "action" in form.attrs:
        action_url = form["action"]
    else:
        print("Invalid URL. Please provide a valid 1fichier URL.")
        return None
    
    if input and "value" in input.attrs:
        adz = input["value"]
    else:
        print("Invalid URL. Please provide a valid 1fichier URL.")
        return None
    
    extract_direct_urls(action_url, adz)


def handle_bulk_urls(file_path):
    if not os.path.isfile(file_path):
        print("Invalid file path. Please provide a valid text file containing 1fichier URLs.")
        return

    with open(file_path, "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        extract_form_values(url)


def main():
    if len(sys.argv) < 2:
        print("Please use '-bulk' with the file path for bulk direct URL extraction.")
        return

    if sys.argv[1] == "-bulk":
        if len(sys.argv) < 3:
            print("Please provide the file path for bulk direct URL extraction.")
            return
        else:
            file_path = sys.argv[2]
            handle_bulk_urls(file_path)
    
    else:
        url = sys.argv[1]
        extract_form_values(url)

if __name__ == "__main__":
    main()