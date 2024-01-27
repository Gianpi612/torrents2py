# torrents2py

Torrents2py is a simple Python package for searching and retrieving torrent details from Torrentz2.nz. Easily access and manage torrent information in your Python projects.

# Overview

**torrents2py** is a Python package designed to simplify the process of searching for and retrieving information about torrents from the Torrentz2 website. It provides a convenient interface for programmatically interacting with Torrentz2, allowing users to search for torrents and fetch details based on specific criteria.

## Key Features

- **Search Torrents:** Utilize the `search_torrents` function to perform searches for torrents based on a provided search query and optional filters.

- **Filtering Options:** Apply filters such as minimum seeds, minimum peers, and maximum pages to refine search results.

- **Retrieve Torrent Details:** Obtain details for each matching torrent, including title, upload date, size, seeds, peers, and magnet link.

- **Magnet Links:** Retrieve magnet links for found torrents, simplifying downloads.

## Installation

To install the package, run the following command:

```bash
pip install torrents2py
```

# Usage
If you wish to search for torrents, it's as straightforward as:
```python
from torrents2py import search_torrents

# The search_torrents function returns a tuple with two elements:
# - results: a list of dictionaries, each containing information about a torrent,
#            including Title, Uploaded, Size, Seeds, Peers, etc.
# - magnet_links: a list of magnet links corresponding to each torrent in the results.

results, magnet_links = search_torrents("Search input")

```

If you'd like to print all information about the found torrents, you can do the following:

```python
from torrents2py import search_torrents

# Perform a search without filters
results, magnet_links = search_torrents("Search input")

# Print Title, upload time, size, seeds, peers and magnet_links
print("\nSearch Results:")
for index, result in enumerate(results, start=1):
    print(f"\nTorrent {index} Information:\n"
          f"   Title:    {result['Title']}\n"
          f"   Uploaded: {result['Uploaded']}" + " ago\n"
          f"   Size:     {result['Size']}\n"
          f"   Seeds:    {result['Seeds']}\n"
          f"   Peers:    {result['Peers']}\n"
          f"   Magnet Link: {magnet_links[index - 1]}\n")
```

## Search with filters
If you wish to search your torrent with specific filters, such as minimum seeds, minimum peers, page, maximum pages and more you can achieve this by:

```python
# Filters, as of torrents2py v0.2 these are all the suppported filters:
filters = {
    # Filter torrents with a minimum of 2 seeds - Default is 0
    'min_seeds': 2,
    # Filter torrents with a minimum of 2 peers - Default is 0
    'min_peers': 2,
    # Filter torrents with a minimum of 7 GB - Default is 0 bites
    # both min_size and max_size support B, KB, MB, GB, TB. (case-insensitive as shown)
    'min_size': '7Gb',
    # Filter torrents with a maximum of 10 GB - Default is unlimited
    'max_size': '10gB',
    # Specify the page number for torrent search results - Default is 1
    'page': 1,
    # Set the maximum number of pages to retrieve for torrent search results
    # - If max page is not provided it will only fetch 1 page of torrents
    'max_pages': 50,
    # Exclude specific words from the search
    'exclude_keywords': ['bella', "ciao"],  
}

# Pass filters to search_torrents to perform a search with the specified filters
results, magnet_links = search_torrents("Search input", filters)

print("\nFiltered Search Results:")
for index, result in enumerate(results, start=1):
    print(f"\nTorrent {index} Information:\n"
          f"   Title:    {result['Title']}\n"
          f"   Uploaded: {result['Uploaded']}\n"
          f"   Size:     {result['Size']}\n"
          f"   Seeds:    {result['Seeds']}\n"
          f"   Peers:    {result['Peers']}\n"
          f"   Magnet Link: {magnet_links[index - 1]}\n")

```


