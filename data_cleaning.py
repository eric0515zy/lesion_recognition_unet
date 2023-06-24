# This code is to delete redundant files in the downloaded traning samples from ISIC.

import os

folder_path = r"D:\UCSD\ECE285\ISIC-2017_Validation_Data\ISIC-2017_Validation_Data"

# Iterate over the files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    # Check if the file is a PNG image
    if file_name.lower().endswith(".png"):
        #Delete the PNG file
        os.remove(file_path)
print("done")