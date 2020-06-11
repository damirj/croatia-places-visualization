# Croatia Places Visualization

Visualization of similarities in settlement names in Croatia

App available [here!](https://damirj.github.io/croatia-places-visualization/)

### How to use the app:
Select sufix or prefix depending on what are you looking (end or start of the settlement name). After that type in the letters you are interested in and click "Add" if you want to save the result. Click the red "X" if you want to remove the specific result.

* **croatia_places.py** : Fetching all settlements using OpenStreetMap API and saving it to places.txt
* **parser.py** : Parsing from places.txt to GeoJson format (parsed.txt)
* **parsed.json** : Formated into JSON template
* **parsedTopojson.json** : "parsed.json" -> From GeoJson to TopoJson format
* **cro.json** : TopoJson file for shape of Croatia
* **index.html** : using d3.js fetching json files and displaying them

