import sys
import os
import requests
from bs4 import BeautifulSoup


def extract_1fichier_url(url):
    with requests.get(url) as response:
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        namehost_value = "1fichier.com"
        button_element = soup.find("button", attrs={"namehost": namehost_value})

        if button_element and "link" in button_element.attrs:
            link_value = button_element["link"]
            return link_value
        else:
            return None


def extract_bulk_urls(file_path):
    if not os.path.isfile(file_path):
        print("Invalid file path. Please provide a valid text file containing MultiUp URLs.")
        return

    with open(file_path, "r") as file:
        urls = file.readlines()

    output = open('1fichier.txt', 'a')

    for url in urls:
        url = url.strip().replace("download", "mirror")
        extracted_url = extract_1fichier_url(url)
        if extracted_url:
            print(extracted_url)
            output.write(extracted_url + "\n")
            output.flush()


def main():
    if len(sys.argv) < 2:
        print("Please provide the MultiUp file URL or use '-bulk' for bulk URL extraction.")
        return

    if sys.argv[1] == "-bulk":
        if len(sys.argv) < 3:
            print("Please provide the file path for bulk URL extraction.")
            return
        else:
            file_path = sys.argv[2]
            output_urls = extract_bulk_urls(file_path)
    else:
        url = sys.argv[1].replace("download", "mirror")
        extract_1fichier_url(url)


if __name__ == "__main__":
    main()