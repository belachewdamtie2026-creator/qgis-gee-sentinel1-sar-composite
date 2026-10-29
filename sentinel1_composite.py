import ee
from ee_plugin import Map

# 1. Fetch the official country boundary for Ethiopia from GEE
ethiopia_boundary = (ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
                     .filter(ee.Filter.eq('country_na', 'Ethiopia')))

# Use this national geometry as our Area of Interest (AOI)
aoi = ethiopia_boundary.geometry()

# 2. Query and Filter the Sentinel-1 SAR Image Collection
s1_collection = (ee.ImageCollection('COPERNICUS/S1_GRD')
                 .filterBounds(aoi)
                 .filterDate('2026-01-01', '2026-10-29')
                 .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
                 .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
                 .filter(ee.Filter.eq('instrumentMode', 'IW')))

# 3. Calculate a median composite to clean up cloud/orbit gaps across the country
s1_image = s1_collection.median()

# 4. Create the RGB composite using VV, VH, and the ratio (VV/VH)
vv = s1_image.select('VV')
vh = s1_image.select('VH')
ratio = vv.divide(vh).rename('VV_VH_ratio')

# Clip the final image strictly to the borders of Ethiopia
rgb_composite = ee.Image.cat([vv, vh, ratio]).clip(aoi)

# 5. High-contrast visualization parameters for radar backscatter
vis_params = {
    'bands': ['VV', 'VH', 'VV_VH_ratio'],
    'min': [-20, -25, 0.1],
    'max': [0, -5, 1],
    'gamma': 1.2
}

# 6. Add the nationwide layer to your QGIS layers panel
Map.addLayer(rgb_composite, vis_params, 'Sentinel-1 SAR - Full Ethiopia')
print("Nationwide Sentinel-1 composite added to canvas!")
