# torrents2py

Torrents2py is a simple Python package for searching and retrieving torrent details from Torrentz2.nz. Easily access and manage torrent information in your Python projects.

# Overview

**torrents2py** is a Python package designed to simplify the process of searching for and retrieving information about torrents from the Torrentz2 website. It provides a convenient interface for programmatically interacting with Torrentz2, allowing users to search for torrents and fetch details based on specific criteria.

## Key Features

- **Search Torrents:** Utilize the `search_torrents` function to perform searches for torrents based on a provided search query and optional filters.

- **Filtering Options:** Apply filters such as minimum seeds, minimum peers, and maximum pages to refine search results.

- **Retrieve Torrent Details:** Obtain details for each matching torrent, including title, upload date, size, seeds, peers, and magnet link.

## Installation

To install the package, run the following command:

```bash
pip install torrents2py
```

# Usage
If you wish to search for torrents, it's as straightforward as:
```python
from torrents2py import search_torrents

# The search_torrents function returns a tuple with one element:
# - results: a list of dictionaries, each containing information about a torrent,
#            including Title, Uploaded, Size, Seeds, Peers and magnet links.

results = search_torrents("Search input")

```

If you'd like to print all information about the found torrents, you can do the following:

```python
from torrents2py import search_torrents

# Perform a search without filters
results = search_torrents("Search input")

# Print Title, upload time, size, seeds, peers and magnet_links
print("\nSearch Results:")
for index, result in enumerate(results, start=1):
    print(f"Torrent {index} Information:"
            f"\n   Title:    {result.get('Title')}"
            f"\n   Uploaded: {result.get('Uploaded')}"
            f"\n   Size:     {result.get('Size')}"
            f"\n   Seeds:    {result.get('Seeds')}"
            f"\n   Peers:    {result.get('Peers')}"
            f"\n   Magnet Link:    {result.get('MagnetLink')}")
```

## Search with filters
If you wish to search your torrent with specific filters, such as minimum seeds, minimum peers, page, maximum pages and more you can achieve this by:

```python
# Filters, these are all the supported filters:
filters = {
    # Filter torrents with a minimum of 2 seeds
    'min_seeds': 2,

    # Filter torrents with a minimum of 2 peers
    'min_peers': 2,

    # Filter torrents with a minimum size and a maximum size
    # Both min_size and max_size support B, KB, MB, GB, TB (case-insensitive as shown)
    'min_size': '7GB',
    'max_size': '10gb',

    # Minimum upload time for torrents in a search
    'min_upload': "1 second",

    # Maximum upload time for torrents in a search
    'max_upload': "2 months",

    # Specify the page number for torrent search results
    'page': 1,

    # Set the maximum number of pages to retrieve for torrent search results (page + max_pages)
    # If max_pages is not provided, it will only fetch the first page of torrents
    'max_pages': 3,

    # Exclude specific words from the search
    'exclude_keywords': ['bella', 'ciao'],

    # Sort by upload time:
    # support are upload, peers, seeds or size
    'sort_by': ['upload', 'peers', 'seeds', 'size'],

    # Sort order for search results: 'asc' for ascending, 'desc' for descending
    'sort_order': 'desc',
}

# Perform a search with the specified filters
results = search_torrents("c", filters)

print("\nFiltered Search Results:")
for index, result in enumerate(results, start=1):
    print(f"Torrent {index} Information:"
          f"\n   Title:    {result.get('Title')}"
          f"\n   Uploaded: {result.get('Uploaded')}"
          f"\n   Size:     {result.get('Size')}"
          f"\n   Seeds:    {result.get('Seeds')}"
          f"\n   Peers:    {result.get('Peers')}"
          f"\n   Magnet Link:    {result.get('MagnetLink')}")


```


