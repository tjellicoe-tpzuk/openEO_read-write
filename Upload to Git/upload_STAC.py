from openeo.udf import XarrayDataCube
import xarray as xr
from github import Github
import rioxarray
from git_access import git_access_token
from datetime import datetime as dt
import time

def apply_datacube(cube: XarrayDataCube, context: dict):
    xarrayTest = cube.to_array()
    access_token = "please_insert_token"
    url = create_STAC(xarrayTest, access_token)
    return url


def create_STAC(cube: xr.DataArray, access_token: str):
    g = Github(access_token)
    repo = g.get_repo('tjellicoe-tpzuk/openEO_read-write')
    outfile = cube.to_netcdf()
    todayDate = dt.now().strftime("%y-%m-%d")
    timeNow = time()[-6:]
    fileName = f"openEO_output_{timeNow}"
    repo.create_file(f'data/{fileName}.nc', 'upload tif', outfile, branch='main')
    #print(repo)
    url = "https://raw.githubusercontent.com/tjellicoe-tpzuk/openEO_read-write/main/data/" + fileName + ".nc"
    
    return url


if __name__ == "__main__":
    geotiff_path_red = "/home/tjellicoe/Documents/EOEPCA-and-OPENEO/useful scripts/B01.tif"

    xarrayTest = rioxarray.open_rasterio(geotiff_path_red).to_dataset('band').to_dataarray()
    print(dt.now().strftime("%y-%m-%d"))
    create_STAC(xarrayTest, git_access_token)
