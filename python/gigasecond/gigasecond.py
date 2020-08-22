from datetime import timedelta


def add(moment):
    GIGASECOND = 1_000_000_000
    return moment + timedelta(seconds=GIGASECOND)
