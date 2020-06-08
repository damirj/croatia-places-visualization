def formJSON(place):
    json = '{"type": "Feature", "properties":{"name": "' + str(place[0]) + '"}, "geometry":{ "type": "Point","coordinates": [ ' + str(place[3]) + ', ' + str(place[2]) + ' ]}},'
    return json


def read_parse(filename):
    f = open(filename,  encoding="utf8", mode="r")
    src = f.read()
    rows = src.split("\n")

    places = []
    for row in rows:
        place = row.split(",")
        place[2] = float(place[2])
        place[3] = float(place[3])
        if (place[2] > 40 and place[2] < 49) and (place[3] > 13 and place[3] < 20):
            places.append(place)

    f.close()
    return places


def write_and_save(filename, data):
    handle = open(filename, encoding="utf8", mode="w")
    start = '{"type": "FeatureCollection","features": ['
    end = ']}'

    handle.write(start)

    for place in data:
        handle.write(formJSON(place))

    handle.write(end)

    handle.close()


filename = "placesUpdate.txt"
places = read_parse(filename)
write_and_save("parsedUpdate.txt", places)