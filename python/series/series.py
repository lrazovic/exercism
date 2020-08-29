from typing import List


def slices(series: str, length: int) -> List[str]:
    if length < 1 or length > len(series):
        raise ValueError("Error in length")
    return [series[i : i + length] for i in range(len(series) - length + 1)]

