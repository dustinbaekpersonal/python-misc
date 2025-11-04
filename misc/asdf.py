import math
import re

import requests

def fetch_data(url: str) -> None:
    """
    Main entrypoint to print out the string.

    Args:
        url (str): url to fetch html data which contains x,y-coord and character
    
    Returns:
        prints out characters in stdout
    """
    response = requests.get(url)
    response.raise_for_status()

    html = response.text
    lines = re.findall(r'<p[^>]*>(.*?)</p>', html)
    filtered_lines = _filter_lines(lines)
    data = _clean_data(filtered_lines)

    if (data_length:=len(data)) % 3:
        raise ValueError(f"Cleaned data should be multiple of 3, but currently: {data_length}")

    grid_map = {}
    min_x = min_y = math.inf
    max_x = max_y = -math.inf

    for i in range(0, len(data), 3):
        x = int(data[i])
        char = data[i + 1]
        y = int(data[i + 2])

        grid_map[(x,y)] = char

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    if not grid_map:
        print(f'No data to show from given URL: {url}')
        return
    
    for y in range(max_y, min_y - 1, -1):
        row = ''.join(grid_map.get((x, y), ' ') for x in range(min_x, max_x + 1))
        print(row) 

def _filter_lines(lines: list[str]) -> list[str]:
    """Filter out unnecessary html parsed lines."""
    to_be_seen = {"x-coordinate", "Character", "y-coordinate"}
    for idx, line in enumerate(lines):
        clean_line = re.sub(r'<.*?>', '', line).strip()

        if clean_line in to_be_seen:
            to_be_seen.remove(clean_line)
        if not to_be_seen:
            filtered_lines = lines[idx+1:]
            break

    if to_be_seen:
        raise ValueError(f"Passed URL of {url} doesn't contain either one or many of {to_be_seen}.")
    return filtered_lines

def _clean_data(filtered_lines: list[str]) -> list[str]:
    """Clean the html parsed data to only contain coordinates and character."""
    clean_data = []
    for line in filtered_lines:
        val = re.sub(r'<.*?>', '', line).strip()
        if val:
            clean_data.append(val)
    return clean_data


if __name__ == "__main__":
    # url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"
    fetch_data(url=url)