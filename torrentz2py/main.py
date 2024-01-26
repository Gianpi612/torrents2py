import requests
from bs4 import BeautifulSoup


def convert_to_int(value):
    """
    Convert a string representation of a numerical value to an integer.

    This function is designed for parsing and converting numerical values
    representing the number of seeds or peers within Torrentz2 torrent listings.
    It handles cases where the number of seeds/peers is suffixed with 'K' (representing a thousand).
    For example, '1.3K' will be converted to 1300. If the conversion is not possible,
    it returns 0.

    Parameters:
    - value (str): The input string to be converted.

    Returns:
    - int: The converted integer value.
    """
    if 'K' in value:
        return float(value[:-1]) * 1000
    else:
        try:
            return int(value)
        except ValueError:
            return 0


def get_torrents(search_query, current_page=1, min_seeds=0, min_peers=0, max_pages=None):
    """
    Get torrent details and magnet links from Torrentz2.

    Parameters:
    - search_query (str): The search query for torrents.
    - current_page (int): The current page of search results (default is 1).
    - min_seeds (int): The minimum number of seeds for filtering (default is 0).
    - min_peers (int): The minimum number of peers for filtering (default is 0).
    - max_pages (int): The maximum number of pages to retrieve (default is None, which fetches 1 page).

    Returns:
    - tuple: A tuple containing a list of torrent details and a list of magnet links.
    """
    base_url = 'https://torrentz2.nz/search?q=' + search_query
    torrent_details = []
    torrent_magnet_links = []

    try:
        for page in range(current_page, current_page + (max_pages or 1)):
            current_url = f"{base_url}&page={page}"
            response = requests.get(current_url)
            response.raise_for_status()  # Raises an exception in case of HTTP error

            soup = BeautifulSoup(response.text, 'html.parser')
            torrent_entries = soup.find_all('dl')

            # If there are no torrents on the page, stop the search
            if not torrent_entries:
                break

            for entry in torrent_entries:
                title = entry.find('a', {'target': '_blank'}).text.strip()
                uploaded = entry.find('span', {'title': True}).text.strip()
                size = entry.find_all('span')[2].text.strip()
                seeds = convert_to_int(entry.find_all('span')[3].text.strip())
                peers = convert_to_int(entry.find_all('span')[4].text.strip())

                magnet_span = entry.find('span')
                if magnet_span and magnet_span.find('a'):
                    magnet_link = magnet_span.find('a')['href']

                    # Apply filters on seeds and peers
                    if seeds >= min_seeds and peers >= min_peers:
                        torrent_details.append({
                            "Title": title,
                            "Uploaded": uploaded,
                            "Size": size,
                            "Seeds": seeds,
                            "Peers": peers,
                            "MagnetLink": magnet_link
                        })
                        torrent_magnet_links.append(magnet_link)

    except requests.exceptions.RequestException as e:
        # Handle exceptions related to HTTP requests
        print(f"Error in the HTTP request: {e}\n"
              f"This error can only mean 2 things:\n"
              f"1. You don't have internet access\n"
              f"2. Torrentz2 is currently down\n")

    except (AttributeError, TypeError) as e:
        # Handle exceptions related to HTML parsing
        print(f"Error parsing, the structure of Torrentz2 might have changed: {e}\n"
              f"If you encounter this error, please open a GitHub issue.")

    except Exception as e:
        # Handle other unexpected exceptions
        print(f"Unexpected error: {e}\n"
              f"If you encounter this error, please open a GitHub issue.")

    return torrent_details, torrent_magnet_links


def search_torrents(search_query, filters=None):
    """
    Search for torrents with optional filters.

    Parameters:
    - search_query (str): The search query for torrents.
    - filters (dict): Dictionary of filters, including page, min_seeds, min_peers, and max_pages.

    Returns:
    - tuple: A tuple containing a list of torrent details and a list of magnet links.
    """
    if filters is None:
        filters = {}

    page = filters.get('page', 1)
    min_seeds = filters.get('min_seeds', 0)
    min_peers = filters.get('min_peers', 0)
    max_pages = filters.get('max_pages', None)

    try:
        torrent_details, internal_magnet_links = get_torrents(
            search_query, page, min_seeds, min_peers, max_pages
        )

        if not torrent_details:
            return [], []

        return torrent_details, internal_magnet_links

    except Exception as e:
        # Handle general exceptions
        print(f"Error during the search for torrents: {e}")
        return [], []
