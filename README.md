# MultiUp to 1fichier URL Extractor

This is a simple Python tool that extracts 1fichier URLs from MultiUp URLs. It utilizes BeautifulSoup for web scraping to find and extract the 1fichier download links.

## How to Use

1. Clone or download this repository.
2. Install the required dependencies by running the following command:
```pip install -r requirements.txt```

3. Run the script with the following command:
```python extract_urls.py <MULTIUP_URL>```

Replace `<MULTIUP_URL>` with the URL of the MultiUp page containing the links you want to extract. The script will output the 1fichier URLs to a file named `output.txt`.

If you want to extract multiple URLs in bulk, you can use the `-bulk` option and provide a text file containing the list of MultiUp URLs. Each URL should be on a separate line.

```python extract_urls.py -bulk <FILE_PATH>```

Replace `<FILE_PATH>` with the path to the text file containing the list of MultiUp URLs. The script will extract the 1fichier URLs and store them in the `output.txt` file.

## Example

Suppose you have a MultiUp URL: _https://multiup.org/download/123456abcdef_. To extract the 1fichier URL, run the following command: ```python extract_urls.py https://multiup.org/download/123456abcdef```

The extracted 1fichier URL will be saved to the `output.txt` file.

## Disclaimer

This tool is intended for personal use only. Make sure to respect the terms of service of the websites you are scraping. The authors of this tool are not responsible for any misuse or violation of third-party website policies.

## License

This project is licensed under the GNU GENERAL PUBLIC License - see the [LICENSE](LICENSE) file for details.


