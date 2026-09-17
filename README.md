# Tunisia-Vegetation-Web-Map
# Tunisia Drought Early Warning System

An interactive web-based mapping application designed to display **governorate-level geographic and attribute data for Tunisia**.

The application uses Leaflet to display an interactive map and loads Tunisia governorate boundaries from an ESRI Shapefile (`.shp`, `.shx`, `.dbf`, `.prj`). The Shapefile is retrieved from a GitHub repository and converted to GeoJSON directly in the browser using `shpjs`.

## Features

* Interactive map of Tunisia.
* Governorate-level geographic boundaries.
* OpenStreetMap base map.
* Governorate boundaries loaded dynamically from a remote GitHub repository.
* Shapefile processing directly in the browser.
* Hover effect when moving over a governorate.
* Clickable governorates.
* Governorate attribute information displayed in a sidebar.
* Automatic map zoom to the Tunisia governorates layer.
* Loading message while geographic data is being retrieved.
* Error handling for missing or invalid Shapefile data.
* No backend server is required for the map application itself.

## Technologies Used

* **HTML5** – Webpage structure.
* **CSS3** – User interface and layout.
* **JavaScript** – Application logic and data processing.
* **Leaflet 1.9.4** – Interactive web mapping.
* **shpjs** – Reading and converting Shapefiles to GeoJSON.
* **OpenStreetMap** – Base map tiles.
* **GitHub** – Hosting the Shapefile data.

Leaflet and shpjs are loaded from external CDNs.

## Project Structure

A basic project structure can be:

```text
project/
│
├── index.html
└── README.md
```

The geographic data does not need to be stored directly inside the project because the application retrieves it from a remote GitHub repository.

The expected remote directory contains:

```text
Tunisia_shapefiles/
│
├── Tunisia_gov.shp
├── Tunisia_gov.shx
├── Tunisia_gov.dbf
└── Tunisia_gov.prj
```

## Data Sources

The application uses four components of an ESRI Shapefile:

| File   | Purpose                                              |
| ------ | ---------------------------------------------------- |
| `.shp` | Contains the geographic shapes/geometries            |
| `.shx` | Contains the shape index                             |
| `.dbf` | Contains attribute information                       |
| `.prj` | Contains the coordinate reference system information |

All four files are downloaded before the governorate layer is created.

## How It Works

### 1. Initialize the Map

The application creates a Leaflet map centered over Tunisia:

```javascript
const map = L.map("map").setView(
    [33.8, 9.5],
    6
);
```

A zoom level of `6` provides an initial view covering Tunisia.

### 2. Add the Base Map

OpenStreetMap tiles are used as the background map:

```javascript
L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        maxZoom: 18,
        attribution:
            "&copy; OpenStreetMap contributors"
    }
).addTo(map);
```

This provides geographical context behind the governorate boundaries.

### 3. Retrieve the Shapefile

The application defines a base URL for the remote Shapefile data:

```javascript
const BASE_URL =
    "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/Tunisia_shapefiles/";
```

The `YOUR_USERNAME` and `YOUR_REPOSITORY` values must be replaced with the actual GitHub username and repository name.

The application then creates URLs for:

```text
Tunisia_gov.shp
Tunisia_gov.shx
Tunisia_gov.dbf
Tunisia_gov.prj
```

### 4. Download the Files

The application uses `fetch()` to retrieve the files.

Binary files such as `.shp`, `.shx`, and `.dbf` are downloaded as `ArrayBuffer` objects, while the `.prj` file is downloaded as text.

The four files are downloaded simultaneously using `Promise.all()`, which allows the application to retrieve the required data efficiently.

## Shapefile Processing

After downloading the files, the application uses `shpjs` to process the Shapefile.

The geometry is extracted from the `.shp` file:

```javascript
const geometries =
    shpjs.parseShp(
        shpBuffer,
        prjText
    );
```

The attribute information is extracted from the `.dbf` file:

```javascript
const properties =
    shpjs.parseDbf(
        dbfBuffer
    );
```

The geometries and attributes are then combined into a GeoJSON object:

```javascript
const geojson =
    shpjs.combine([
        geometries,
        properties
    ]);
```

This GeoJSON object can then be displayed using Leaflet.

## Governorate Layer

The converted GeoJSON is added to the map using `L.geoJSON()`.

Each governorate is given a default style:

* Border color: dark gray
* Border width: 1
* Fill color: blue
* Fill opacity: 0.25

When the user moves the mouse over a governorate, the border becomes thicker and the fill becomes more visible.

When the mouse leaves the governorate, the original style is restored.

## Governorate Selection

Governorates are interactive.

When a user clicks on a governorate, the application's `showGovernorate()` function receives the feature's attribute information.

The sidebar is then populated with all available attributes from the Shapefile.

For example, if the Shapefile contains attributes such as:

```text
NAME
CODE
REGION
AREA
```

these values will be displayed automatically.

The application does not require the attribute fields to be hard-coded because it uses:

```javascript
Object.keys(properties)
```

to iterate through the available properties.

## Sidebar

The right side of the application contains a sidebar titled:

**Governorate Data**

Initially, it displays:

> Loading governorates...

After the data has loaded successfully, it displays:

> Click a governorate on the map.

After a governorate is selected, its available attribute information is displayed in the sidebar.

## Error Handling

The application includes error handling for problems that may occur while loading the geographic data.

Possible errors include:

* Shapefile files cannot be downloaded.
* The GitHub URL is incorrect.
* A required Shapefile component is missing.
* The `shpjs` library fails to load.
* The Shapefile contains no features.
* The remote server returns an HTTP error.

If an error occurs, the sidebar displays a message containing:

* The error type.
* The error message.

For example:

```text
Shapefile Error

HTTP 404: [URL]
```

## Requirements

The application requires:

* A modern web browser.
* An internet connection.
* Access to the GitHub repository containing the Shapefile.
* Access to the Leaflet and shpjs CDN resources.

No database or backend API is required by the current implementation.

## Configuration

Before running the application, update:

```javascript
const BASE_URL =
    "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/main/Tunisia_shapefiles/";
```

Replace:

```text
YOUR_USERNAME
```

with your GitHub username and:

```text
YOUR_REPOSITORY
```

with the name of your GitHub repository.

For example:

```javascript
const BASE_URL =
    "https://raw.githubusercontent.com/example/example-repository/main/Tunisia_shapefiles/";
```

Make sure that the following files exist in that directory:

```text
Tunisia_gov.shp
Tunisia_gov.shx
Tunisia_gov.dbf
Tunisia_gov.prj
```

## Running the Application

### Option 1 — Local Web Server

It is recommended to run the application through a local web server rather than opening the HTML file directly.

If Python is installed, open a terminal in the project directory and run:

```bash
python3 -m http.server
```

Then open:

```text
http://localhost:8000
```

### Option 2 — GitHub Pages

The project can also be deployed using GitHub Pages.

The HTML application can be hosted on GitHub Pages while the Shapefile components remain in the repository.

Make sure that the `BASE_URL` points to the correct repository and branch.

## User Workflow

The typical user workflow is:

```text
Open the application
        ↓
Leaflet map is initialized
        ↓
OpenStreetMap tiles are loaded
        ↓
Shapefile components are downloaded
        ↓
SHP + PRJ → geographic geometries
        ↓
DBF → attribute information
        ↓
Geometries + attributes → GeoJSON
        ↓
GeoJSON → Leaflet governorate layer
        ↓
Map automatically fits Tunisia
        ↓
User selects a governorate
        ↓
Governorate attributes appear in the sidebar
```

## Future Improvements

The current application provides the geographic foundation for a drought early warning system. Possible future improvements include:

* Adding drought indicators to each governorate.
* Adding vegetation indices such as NDVI.
* Adding rainfall data.
* Adding temperature and precipitation anomalies.
* Adding drought severity classifications.
* Adding historical drought data.
* Adding time-series charts.
* Adding a date selector.
* Adding interactive drought alerts.
* Adding a color-coded drought risk map.
* Adding a search function for governorates.
* Adding statistical summaries.
* Adding data download functionality.
* Adding a dashboard with multiple environmental indicators.
* Making the sidebar and map more responsive on mobile devices.

## Limitations

The current version primarily provides **interactive visualization of governorate boundaries and their Shapefile attributes**.

Although the application is titled **Tunisia Drought Early Warning System**, the current code does not yet calculate or display a specific drought index or drought risk level. Additional environmental and climatic datasets would be required to implement those functions.

## Credits

### Leaflet

The interactive mapping functionality is provided by Leaflet.

### OpenStreetMap

The base map is provided using OpenStreetMap tiles.

### shpjs

The Shapefile parsing and conversion functionality is provided by shpjs.

## License

This project is intended for educational and/or research purposes.

If the geographic data originates from an external dataset, consult the original data provider's licensing and attribution requirements before redistributing or publishing the data.

## Author

**Tunisia Drought Early Warning System**

An interactive web mapping application for exploring Tunisia's governorates and providing a foundation for drought monitoring and early warning.
