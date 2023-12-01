import xarray as xr
import requests
import json
from openeo.udf import XarrayDataCube

def read_netcdf_from_git(url: str):
    loaded_file_raw = requests.get(url)
    loaded_da = xr.load_dataarray(loaded_file_raw.content)
    print(loaded_da)
    return loaded_da

url = "https://raw.githubusercontent.com/tjellicoe-tpzuk/openEO_read-write/main/data/outfile.nc"
#url = "https://github.com/tjellicoe-tpzuk/openEO_read-write/blob/main/data/outfile.nc"
read_netcdf_from_git(url)


def apply_datacube(cube: XarrayDataCube, context: dict):
    url = context['url']
    return read_netcdf_from_git(url)
