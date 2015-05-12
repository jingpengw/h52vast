# h52vast
transform hdf5 data for VAST anotation

for ubuntu users, run the following command to install some packages:

sudo apt-get install python-numpy python-h5py python-tk python-tifffile spyder

double click the h52vast file, and choose the tif file you want to transfer. the generated hdf5 file could be found in the same folder of input file.

if the h52vast do not pop file choosing window, you probably have to change the file permission. right click and choose the property, you can add execute permission in the "permission" panel.

# compilation step
cython --embed h52vast.py
gcc -o h52vast h52vast.c -I/usr/include/python2.7 -I/usr/people/jingpeng/libs/anaconda/include/ -lpython2.7 -lpthread -lm -lutil -ldl
