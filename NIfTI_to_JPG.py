import nibabel as nib
from PIL import Image
import numpy as np
import gzip
import tempfile
import shutil
import os


def nii_to_jpg(input_folder, slice_index=None):
    filename_images = os.listdir(input_folder)
    for nii_file in zip(filename_images):
        
        print('Image ' + nii_file[0] + ' inProgress...')
        nii_file = os.path.join(input_folder, nii_file[0])

        # Decompress NIfTI file to a temporary location
        # to handel the .gz files
        with gzip.open(nii_file, 'rb') as f_in:
            temp_dir = tempfile.mkdtemp()
            temp_nii_file = os.path.join(temp_dir, 'temp.nii')
            with open(temp_nii_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        # Load NIfTI file
        img = nib.load(temp_nii_file)
        data = img.get_fdata()
        
        # Normalize data
        data = (data - np.min(data)) / (np.max(data) - np.min(data)) * 255
        data = np.uint8(data)

        # Select slice (if not specified or bigger than the third dimension, use the middle slice along the third dimension)
        if slice_index is None or slice_index > data.shape[2]:
            slice_index = data.shape[2] // 2
        selected_slice = data[:, :, slice_index]
        
        # Convert to PIL Image
        image = Image.fromarray(selected_slice, mode='L')  # 'L' mode for grayscale images
        
        # Save as JPEG
        output_file_no_extension = os.path.splitext(nii_file)[0]  # Remove extension
        output_file_no_extension += '.jpg'  # Add .jpg extension

        image.save(output_file_no_extension)

# if __name__ == "__main__":

#     folder = 'D:\\Edu\\Master\\SpineVertebrae\\Datasets\\2019\\Validation'
#     # folder = 'D:\\Edu\\Master\\SpineVertebrae\\Datasets\\Verse2019\\OTI'
#     nii_to_jpg(folder)
