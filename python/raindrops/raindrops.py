def convert(number):
    raindrops = ""
    if not number % 3:
        raindrops += "Pling"
    if not number % 5:
        raindrops += "Plang"
    if not number % 7:
        raindrops += "Plong"
    if raindrops == "":
        return str(number)
    return raindrops
