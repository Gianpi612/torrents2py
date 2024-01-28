import requests
from bs4 import BeautifulSoup
from torrents2py.utils import convert_to_int, convert_to_bytes


def get_torrents(search_query, current_page=1, min_seeds=0, min_peers=0, max_pages=None, min_size=None, max_size=None,
                 exclude_keywords=None, sort_by=None, sort_order=None):
    """
    Get torrent details and magnet links from Torrentz2. From torrents2py v0.5+ magnet links and torrents details are stored in the same dictionary

    Parameters:
    - search_query (str): The search query for torrents.
    - current_page (int): The current page of search results (default is 1).
    - min_seeds (int): The minimum number of seeds for filtering (default is 0).
    - min_peers (int): The minimum number of peers for filtering (default is 0).
    - max_pages (int): The maximum number of pages to retrieve (default is None, which fetches 1 page).
    - min_size (str): The minimum file size (e.g., '1GB').
    - max_size (str): The maximum file size (e.g., '5GB').
    - exclude_keywords (list): List of keywords to exclude from results.
    - sort_by (str): The field by which to sort the results (e.g., 'seeds').
    - sort_order (str): The order of sorting, either 'asc' (ascending) or 'desc' (descending).

    Returns:
    - tuple: A tuple containing a list of torrent details and a list of magnet links.
    """
    base_url = 'https://torrentz2.nz/search?q=' + search_query
    torrent_details = []

    try:
        for page in range(current_page, current_page + (max_pages or 1)):
            current_url = f"{base_url}&page={page}"
            response = requests.get(current_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            torrent_entries = soup.find_all('dl')

            if not torrent_entries:
                break

            for entry in torrent_entries:
                title = entry.find('a', {'target': '_blank'}).text.strip()
                uploaded = entry.find('span', {'title': True}).text.strip()
                size = entry.find_all('span')[2].text.strip()
                seeds = convert_to_int(entry.find_all('span')[3].text.strip())
                peers = convert_to_int(entry.find_all('span')[4].text.strip())

                if exclude_keywords and any(keyword.lower() in title.lower() for keyword in exclude_keywords):
                    continue

                magnet_span = entry.find('span')
                if magnet_span and magnet_span.find('a'):
                    magnet_link = magnet_span.find('a')['href']

                    file_size_bytes = convert_to_bytes(size)
                    if (min_size is None or file_size_bytes >= convert_to_bytes(min_size)) and (
                            max_size is None or file_size_bytes <= convert_to_bytes(
                        max_size)) and seeds is not None and seeds >= min_seeds and peers >= min_peers:
                        torrent_details.append({
                            "Title": title,
                            "Uploaded": uploaded,
                            "Size": size,
                            "Seeds": seeds,
                            "Peers": peers,
                            "MagnetLink": magnet_link
                        })

            sorting_functions = {
                'seeds': lambda x: x['Seeds'],
                'peers': lambda x: x['Peers'],
                'size': lambda x: convert_to_bytes(x['Size'])
            }

            if sort_by in sorting_functions:
                torrent_details = sorted(torrent_details, key=sorting_functions[sort_by],
                                         reverse=(sort_order == 'desc'))

    except requests.exceptions.RequestException as e:
        print(f"Error in the HTTP request: {e}\n"
              f"This error can only mean 2 things:\n"
              f"1. You don't have internet access\n"
              f"2. Torrentz2 is currently down\n")

    except (AttributeError, TypeError) as e:
        print(f"Error parsing, the structure of Torrentz2 might have changed: {e}\n"
              f"If you encounter this error, please open a GitHub issue.")

    except Exception as e:
        print(f"Unexpected error: {e}\n"
              f"If you encounter this error, please open a GitHub issue.")

    return torrent_details


def search_torrents(search_query, filters=None):
    """
    Search for torrents with optional filters.

    Parameters:
    - search_query (str): The search query for torrents.
    - filters (dict): Dictionary of filters, including page, min_seeds, min_peers, max_pages, min_size, max_size, and exclude_keywords.

    Returns:
    - tuple: A tuple containing a list of torrent details and a list of magnet links.
    """
    if filters is None:
        filters = {}

    page = filters.get('page', 1)
    min_seeds = filters.get('min_seeds', 0)
    min_peers = filters.get('min_peers', 0)
    max_pages = filters.get('max_pages', None)
    min_size = filters.get('min_size')
    max_size = filters.get('max_size')
    exclude_keywords = filters.get('exclude_keywords')
    sort_by = filters.get('sort_by')
    sort_order = filters.get('sort_order')

    try:
        torrent_details = get_torrents(
            search_query, page, min_seeds, min_peers, max_pages, min_size=min_size, max_size=max_size,
            exclude_keywords=exclude_keywords, sort_by=sort_by, sort_order=sort_order
        )

        if not torrent_details:
            return [], []

        return torrent_details

    except Exception as e:
        print(f"Error during the search for torrents: {e}")
        return [], []
