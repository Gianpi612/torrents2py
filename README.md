# torrentz2py

Torrentz2Py is a simple Python package for searching and retrieving torrent details from Torrentz2.nz. Easily access and manage torrent information in your Python projects.

# Overview

**torrentz2py** is a Python package designed to simplify the process of searching for and retrieving information about torrents from the Torrentz2 website. It provides a convenient interface for programmatically interacting with Torrentz2, allowing users to search for torrents and fetch details based on specific criteria.

The package was created to streamline torrent search functionality and sets itself apart by offering a straightforward way to integrate torrent search capabilities into Python applications and scripts.

## Key Features

- **Search Torrents:** Utilize the `search_torrents` function to perform searches for torrents based on a provided search query and optional filters.

- **Filtering Options:** Apply filters such as minimum seeds, minimum peers, and maximum pages to refine search results.

- **Retrieve Torrent Details:** Obtain details for each matching torrent, including title, upload date, size, seeds, peers, and magnet link.

- **Magnet Links:** Retrieve magnet links for found torrents, simplifying downloads.

## Installation

To install the package, run the following command:

```bash
pip install torrentz2py
```

# Usage
Basic torrent search
This example demonstrates how to use the torrentz2py package to search for torrents and retrieve information such as title, upload date, size, seeds, peers and magnet links.
```python
from torrentz2py import search_torrents

# Perform a search without filters
results, magnet_links = search_torrents("Search input")

# The search_torrents function returns a tuple with two elements:
# - results: a list of dictionaries, each containing information about a torrent,
#            including Title, Uploaded, Size, Seeds, Peers, etc.
# - magnet_links: a list of magnet links corresponding to each torrent in the results.

# Print search results regardless of whether they are None
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
If we wanted to search for torrents with specific filters, such as minimum seeds, minimum peers, page and maximum pages we could do:

```python
# Filters, this is optional
filters = {
    'min_seeds': 2,     # Filter torrents with a minimum of 2 seeds - Default is 0
    'min_peers': 2,     # Filter torrents with a minimum of 2 peers - Default is 0
    'page': 1,          # Specify the page number for torrent search results - Default is 1
    'max_pages': 5,     # Set the maximum number of pages to retrieve for torrent search results
                        # - If max page is not provided it will show only 1 page of torrents
}

# Perform a search with the specified filters
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


