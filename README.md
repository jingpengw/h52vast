# h52vast
transform hdf5 data for VAST anotation

for ubuntu users, run the following command to install some packages:

sudo apt-get install python-numpy python-h5py python-tk python-tifffile spyder

use spyder to open and run(F5) the h52vast.py, and than choose the file you want to transform. The program should be able to generate a corresponding tif file in the same folder with the same name.



# compilation step
cython --embed h52vast.py
gcc -o h52vast h52vast.c -I/usr/include/python2.7 -I/usr/people/jingpeng/libs/anaconda/include/ -lpython2.7 -lpthread -lm -lutil -ldl
