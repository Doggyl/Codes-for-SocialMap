__author__ = 'liujunyuan'
import linecache

lon_start = 106
lon_end = 107
lat_start = 29
lat_end = 30
filename = '/Users/liujunyuan/Desktop/python/data/sample.txt'

iteration = 0.02
numfile=open(filename)
filenumber = len(open(filename).readlines())+1

# for i in range(1,filenumber,1):
#     the_coordination = linecache.getline(filename ,i)
#
#     the_lon = the_coordination.split('\t')[0]
#     the_lat = the_coordination.split('\t')[1]
#     print the_lon,the_lat

lon_range1 = lon_start
lat_range1 = lat_start
lon_scale = [0]*int((lat_end-lat_start)/iteration)

for j in range(1,int((lon_end-lon_start)/iteration)+1,1):
    lon_range = lon_range1 + 2*iteration
    longitude = lon_start + (2*j-1)*iteration

    for i in range(1,filenumber,1):
        the_coordination = linecache.getline(filename ,i)
        the_lon = float(the_coordination.split('\t')[0])
        the_lat = float(the_coordination.split('\t')[1])
        if lon_range1<= the_lon<= lon_range:
            # print the_lon,lon_range1,'-',lon_range,the_lat
            scale = int(round((the_lat-29)/(2*iteration)))
            lon_scale[scale] += 1
    lon_range1 = lon_range
print lon_scale





            # for k in range(1,int((lat_end-lat_start)/iteration)+1,1):
            #     lat_range = lat_range1 +2*iteration
            #     latitude = lat_start + (2*k-1)*iteration
            #     if lat_range1<= the_lat <=lat_range:
            #         print longitude,latitude
            #         lat_range1 = lat_start
            #         break
            #     lat_range1 = lat_range


numfile.close()