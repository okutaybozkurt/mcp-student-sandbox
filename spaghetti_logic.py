from typing import List

def calculate_values(data: List[float]) -> List[float]:
    """
    Calculate values by applying a multiplier to each item in the input list.

    Args:
        data (List[float]): A list of numeric values to process.

    Returns:
        List[float]: A list of calculated values.
    """
    return [item * 1.15 for item in data]

def format_values(values: List[float]) -> List[str]:
    """
    Format calculated values into strings.

    Args:
        values (List[float]): A list of numeric values to format.

    Returns:
        List[str]: A list of formatted strings.
    """
    return [f"Total: {value:.2f}" for value in values]

def log_values(values: List[float], file_path: str = "log.txt") -> None:
    """
    Log calculated values to a file.

    Args:
        values (List[float]): A list of numeric values to log.
        file_path (str): The path to the log file. Defaults to "log.txt".
    """
    with open(file_path, "a", encoding="utf-8") as log_file:
        log_file.write(str(values) + "\n")
        
def process_data(data: List[float]) -> List[float]:
    """
    Process input data by calculating, formatting, and logging values.

    Args:
        data (List[float]): A list of numeric values to process.

    Returns:
        List[float]: A list of calculated values.
    """
    calculated_values = calculate_values(data)
    formatted_values = format_values(calculated_values)

    for formatted_value in formatted_values:
        print(formatted_value)

    log_values(calculated_values)
    return calculated_values
