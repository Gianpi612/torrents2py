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

    This function supports Torrentz2.nz's different units: from B, KB, MB, GB to TB.

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


def convert_to_seconds(time_str):
    """
    Converts a string representation of time to seconds.
    Handles cases like "a day", "2 days", "a month", "2 months", etc.

    Args:
    - time_str (str): The string representation of time.

    Returns:
    - int: The equivalent time in seconds.
    """
    # Mapping of time units to their equivalent in seconds
    TIME_UNITS = {
        'second': 1,
        'minute': 60,
        'hour': 60 * 60,
        'day': 24 * 60 * 60,
        'week': 7 * 24 * 60 * 60,
        'month': 30 * 24 * 60 * 60,
        'year': 365 * 24 * 60 * 60,
    }

    # Split the input time string into its numerical part and unit part
    parts = time_str.split()

    # Check if the input string has exactly two parts and the first part is either a number or 'a'/'an'
    if len(parts) != 2 or (not parts[0].isdigit() and parts[0] not in ['a', 'an']):
        raise ValueError(f"Invalid time string: {time_str}")

    # Determine the numeric value and unit from the input parts
    # If the first part is 'a' or 'an', set the numeric value to 1; otherwise, convert it to an integer
    num = 1 if parts[0] in ['a', 'an'] else int(parts[0])
    unit = parts[1].lower()

    # Check if the unit ends with 's' and if so, remove it
    if unit.endswith('s') and unit[:-1] in TIME_UNITS:
        unit = unit[:-1]

    # Check if the unit is in the mapping
    # If it is, return the converted time value in seconds
    # Otherwise, raise an exception for an unsupported time unit (the website was probably modified)
    if unit in TIME_UNITS:
        return num * TIME_UNITS[unit]
    else:
        raise ValueError(f"Unsupported time unit: {unit}")
