# openEO_read-write

This Repo serves as a location that can be written to a read from remotely via a Python script that can be run elsewhere. This allows files to be passed between applications, e.g. from an openEO environment into an EOEPCA execution and back.  
The script located under `/Upload to Git` can be used to remotely add files to the `/data` directory under this repository while the script under `Download from Git` can be used to read and download files from the `/data` directory.

### Use Case
The primary use-case here is for these Python scripts to be as User-Define Functions within [openEO](https://processes.openeo.org/#run_udf) and this will allows data to be extracted from an openEO environment for external processing and then exported back into the openEO environment for further processing within the application.
Note, this is currently only a proof of concept as the openEO runtime environment will need updating before these scripts can run as expected within the openEO environment itself.
