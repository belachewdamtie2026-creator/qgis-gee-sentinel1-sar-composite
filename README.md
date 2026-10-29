# QGIS GEE Sentinel-1 SAR Composite Pipeline

A Python script for the QGIS Python Console (`PyQGIS`) that automates the generation of a seamless, cloud-free, nationwide **Sentinel-1 SAR dual-polarization composite** for Ethiopia using the Google Earth Engine (GEE) API.

## Features
* **Automated Boundary Fetching:** Uses official USDOS international boundaries to pull regional data seamlessly without manual shapefiles.
* **Dual-Polarization RGB Composite:** Combines **VV**, **VH**, and a custom backscatter math ratio (**VV/VH**) to produce a high-contrast radar visualization.
* **Server-Side Processing:** Leverages Google Earth Engine computation directly within the QGIS interface via a plugin bridge.

##  Prerequisites
Before running the script, ensure you have set up your environment:
1. Open QGIS and navigate to `Plugins` > `Manage and Install Plugins...`
2. Search for and install the **Google Earth Engine plugin**.
3. Authenticate your GEE account through the plugin prompts.

##  Usage
1. Open the QGIS Python Console (`Plugins` > `Python Console` or `Ctrl + Alt + P`).
2. Create a new script tab, paste the code from `sentinel1_composite.py`, and hit **Run**.

##  Sample Output
*The script automatically crops and streams high-contrast radar backscatter datasets matching national borders:*
- **Bright Yellow/Tan:** Rough geologic terrain, dense vegetation canopy, and mountain topography (e.g., Ethiopian Highlands, Danakil Depression).
- **Deep Blue/Black:** Smooth features causing specular reflection like lakes, rivers, or open reservoirs (e.g., Lake Tana).

##  License
This project is open-source and available under the MIT License.
