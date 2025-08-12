from mcp.server.fastmcp import FastMCP
import os
import json
from datetime import datetime

mcp = FastMCP("WeatherTool")

WEATHER_FILE = os.path.join(os.path.dirname(__file__), "../resources/weather_data.json")

@mcp.resource("resource://weather_check/{start_date}/{end_date}")
def weather_check(start_date: str, end_date: str):
    """
    Checks weather data for a given date range in the month of September 2025.
    :param start_date: Start date in DD format.
    :param end_date: End date in DD format.
    :return: Filtered weather data within the range.
    """
    # try:
    #     start_dt = datetime.strptime(start_date, "%Y/%m/%d").date()
    #     end_dt = datetime.strptime(end_date, "%Y/%m/%d").date()
    # except ValueError:
    #     return "Invalid date format. Use YYYY/MM/DD."

    with open(WEATHER_FILE, "r") as file:
        weather_data = json.load(file)

    result = []
    for entry in weather_data:
        try:
            # entry_date = datetime.strptime(entry["date"], "%Y/%m/%d").date()
            entry_date = entry["date"]
        except (KeyError, ValueError):
            continue

        if start_date <= entry_date <= end_date:
            result.append(entry)

    return result or "No data found for the given date range."

@mcp.tool()
def weather_check_all(start_date: str, end_date: str):    
    """
    Returns weather data for the month of September 2025.
    :return: specific weather data for September 2025. for a given date range.
    """
    with open(WEATHER_FILE, "r") as file:
        weather_data = json.load(file)

    result = []
    for entry in weather_data:
        try:
            # entry_date = datetime.strptime(entry["date"], "%Y/%m/%d").date()
            entry_date = entry["date"]
        except (KeyError, ValueError):
            continue

        if start_date <= entry_date <= end_date:
            result.append(entry)

    return result or "No data found for the given date range."

if __name__ == "__main__":
    print(weather_check("25", "30"))
    mcp.run()

