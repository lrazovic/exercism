def convert(number):
    raindrops = ""
    if not number % 3:
        raindrops += "Pling"
    if not number % 5:
        raindrops += "Plang"
    if not number % 7:
        raindrops += "Plong"
    return str(number) if not raindrops else raindrops
