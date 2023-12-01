from openeo.udf import XarrayDataCube
import xarray as xr
from github import Github
import rioxarray

def apply_datacube(cube: XarrayDataCube, context: dict):
    xarrayTest = cube.to_array()
    create_STAC(xarrayTest)



def create_STAC(cube: xr.DataArray):
    g = Github('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')
    
    repo = g.get_repo('tjellicoe-tpzuk/openEO_read-write')
    outfile = cube.to_netcdf()
    repo.create_file('data/outfile.nc', 'upload tif', outfile, branch='main')


# if __name__ == "__main__":

#     geotiff_path_red = "/home/tjellicoe/Documents/EOEPCA-and-OPENEO/useful scripts/B01.tif"

#     xarrayTest = rioxarray.open_rasterio(geotiff_path_red).to_dataset('band').to_dataarray()

#     create_STAC(xarrayTest)
