# utils.py
# This module contains utility functions for converting numeric values and file sizes.


def convert_to_int(value):
    """
    Convert a string representation of a numerical value to an integer.

    This function is designed for parsing and converting numerical values
    representing the number of seeds or peers within Torrentz2 torrent listings.
    It handles cases where the number of seeds/peers is suffixed with 'K' (representing a thousand).
    For example, '1.3K seeds' will be converted to 1300 seeds. If the conversion is not possible,
    it returns 0. (although t it should never be the case)

    Parameters:
    - value (str): The input string to be converted.

    Returns:
    - int: The converted integer value.
    """
    if 'K' in value:
        return int(float(value[:-1]) * 1000)
    else:
        try:
            return int(value)
        except ValueError:
            return 0


def convert_to_bytes(value):
    """
    Convert a string representation of a file size to an integer representing bytes.

    This function supports different units: from B, KB, MB, GB to TB.

    Parameters:
    - value (str): The input string representing the file size.

    Returns:
    - int: The converted file size in bytes.
    """
    size_multipliers = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3, 'TB': 1024 ** 4}
    value_str, unit = value[:-2], value[-2:].upper()

    try:
        return int(float(value_str) * size_multipliers[unit])
    except (ValueError, KeyError):
        return 0

