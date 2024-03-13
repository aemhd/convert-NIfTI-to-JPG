
Quick Overview
--------------

-  Convert NIfTI images to jpg images.


Dependencies
------------

-  ``nibabel`` : Used for reading NIfTI files.
-  ``Image`` : Used for saving data in jpg format.
-  ``numpy`` : Used for accessing multi-dimensional arrays and matrice.
-  ``gzip`` : Used for accessing compressed file (nii.gz) files.
-  ``tempfile`` : Used for creating and managing temp files while conversion.
-  ``shutil`` : Used for files operations like Copy and Moving.
-  ``os`` : Used for listing directory files.



Assumptions
-----------

This code is working on compressed NIfTI (extension ``.nii.gz``). 
For working on uncompressed NIfTI files, just replace the ``gzip.open`` funtion with ``open``

How to Use
----------

Call the function and only pass the folder that contains the nii.gz files.

**Example:**

.. code:: bash

    nii_to_jpg(folder)

The resulted jpg files will be saved in the same folder.