# openEO_read-write

This Repo serves as a location that can be written to a read from remotely via a Python script that can be run elsewhere. This allows files to be passed between applications, e.g. from an openEO environment into an EOEPCA execution and back.  
The script located under `/Upload to Git` can be used to remotely add files to the `/data` directory under this repository while the script under `Download from Git` can be used to read and download files from the `/data` directory. The `Call EOEPCA` script can then be used to process a cwl file, the example includes a script called [snuggs.cwl](https://raw.githubusercontent.com/EOEPCA/deployment-guide/main/deploy/samples/requests/processing/snuggs.cwl), along with a set of inputs and applies the cwl file to those inputs via the ADES and an execution of EOEPCA.

### Use Case
The primary use-case here is for these Python scripts to be as User-Define Functions within [openEO](https://processes.openeo.org/#run_udf) and this will allows data to be extracted from an openEO environment for external processing and then exported back into the openEO environment for further processing within the application.
The EOEPCA function call will be made after the data has been uploaded to Git and prior to the data being downloaded again. Currently, the `Download from Git` code reads data from a Git repository but this needs to be updated to read from wherever the EOEPCA output is to be stored, often a [Min.io](https://min.io/) bucket. 
Note, this is currently only a proof of concept as the openEO runtime environment will need updating before these scripts can run as expected within the openEO environment itself.

### Process Flow Example
1. openEO loads collection of EO data selected by the user.
2. openEO passes input data, likely in the form of a raster data cube, to a _run_udf_ process node which contains the `Upload to Git` code (we call this Process A). This returns the url pointing to the file saved on a server.
3. Output of Process A is passed to another _run_udf_ process node containing the `Call EOEPCA` code (call this Process B) which executes the selected cwl file on the given file, which will be extracted from the server. This returns another url pointing to the result on a server.
4. The output of Process B is then passed to a final _run_udf_ process node that contains the `Download from Git` code (call this Process C) which extracts the data from the server and saves it back into the openEO environment as a dataarray object.
5. Further processing can be done in the openEO environment using the data imported by Process C.

### Issues
To get the integratoion working as expected we will need to introduce new functionality to convert between datacube-like data and STAC catalog data, as this is required as an input to EOEPCA processing, to conform to the OGC Best Practices.
