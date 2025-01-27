# Jon Zarate
# Shea A. Hess Webber
# Milo Buitrago-Casas
# Exploring the Unseen Sun
# Date Created: 06-21-2023
#
#

# import sunpy
# from sunpy.net import Fido
# from sunpy.net import attrs as a

# jsoc_series = 'hmi.td_fsi_12h'
# jsoc_email = 'jjzarate215@berkeley.edu'
# first_rec = '2023.05.01_00:00:00_TAI'
# last_rec = '2023.05.31_12:00:00_TAI'

fsi_directory = 'C:\\Users\\Jjzar\\OneDrive\\Documents\\ASSURE\\ASSURE 2023\\Exploring the Unseen Sun\\Far-SideImagingData\\May2023'

# query = Fido.search(
#     a.Time(first_rec, last_rec),
#     a.jsoc.Series(jsoc_series),
#     a.jsoc.Notify(jsoc_email)
# )

# print(query)


# download_fsi = Fido.fetch(query, path = fsi_directory)

#########################################################################
import os
from astropy.io import fits
import matplotlib.pyplot as plt
import sunpy.map
from scipy import ndimage
import numpy as np

fsi_images = []
fsi_images_data =[]
fsi_headers = []
avg_may = []
med_may = []

for fits_file in os.listdir(fsi_directory):
    if os.path.isfile(os.path.join(fsi_directory, fits_file)):
        fsi_images.append(fits_file)

        hdu = fits.open(os.path.join(fsi_directory, fits_file))
        image_data = hdu[0].data
        image_header = hdu[0].header['DATE-OBS']
        average_value = hdu[0].header['DATAMEAN']
        median_value = hdu[0].header['DATAMEDN']
        hdu.close()

        fsi_images_data.append(image_data)
        fsi_headers.append(image_header)
        avg_may.append(average_value)
        med_may.append(median_value)



#print(avg_may)

#print(len(avg_may))

#print(med_may)
#print(len(med_may))


plt.scatter(fsi_headers, avg_may, color = 'red')
plt.xlabel('Observed Time')
plt.ylabel('Average Pixel Value')
plt.title('Untitled')
plt.show()


# plt.scatter(fsi_headers, med_may, color = 'red')
# plt.xlabel('Observed Time')
# plt.ylabel('Median Pixel Value')
# plt.title('Untitled')
# plt.show()


##########################################################################
import astropy.units as u



img = 'C:\\Users\\Jjzar\\OneDrive\\Documents\\ASSURE\\ASSURE 2023\\Exploring the Unseen Sun\\Far-SideImagingData\\May2023\\hmi.td_fsi_12h.20230504_000000_TAI.data.fits'

hdulist = fits.open(img)
data = hdulist[0].data

mask = data < data.mean() - data.std() * 2.5

data_masked = data * mask

labeled_array, num_features = ndimage.label(mask)
bounding_boxes = ndimage.find_objects(labeled_array)

centers = []
for box in bounding_boxes:
    y_center = (box[0].start + box[0].stop - 1) / 2
    x_center = (box[1].start + box[1].stop - 1) / 2
    centers.append((x_center, y_center))

labels, n = ndimage.label(mask)
num_dark_spots = n
print("Number of sunspots: ", num_dark_spots)

plt.imshow(data_masked, cmap = "gray", origin = "lower")
plt.colorbar()

x_coord, y_coord = zip(*centers)
plt.scatter(x_coord, y_coord, c = "red", marker = "x")

plt.show()
                                   
# mask = data > data.min() * 0.50

# data2 = ndimage.gaussian_filter(data * ~mask, 14)

# plt.imshow(data2)
# plt.show()

# labels, n = ndimage.label(data2)
# print("Number of regions: ", n)

# map = sunpy.map.Map(img)

# fig = plt.figure()
# ax = plt.subplot(projection = map)
# map.plot()
# plt.show()
# hdulist.close()

