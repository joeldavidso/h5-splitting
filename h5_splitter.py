import h5py
import numpy as np

input_path = "/storage/epp2/phubsg/FTag_samples/ttbar/"

input_h5s = ["user.lbezio.35269581._000001.output.h5",
"user.lbezio.35269581._000002.output.h5",
"user.lbezio.35269581._000003.output.h5"]

#loops over all input h5 files
for i in range(len(input_h5s)):

	#reads the h5 input file
	input = h5py.File(input_path+input_h5s[i], "r")

	#extracts the seperate datasets
	datasets = [input['emtopo'],input['pflow']]
	#creates new h5 files
	emtopo_file = h5py.File('outputs/emtopo_'+str(i)+'.h5', 'w')

	#add datasets to output file
	emtopo_file.create_dataset('jets',
 shape = datasets[0]['jets'].shape,
 dtype = datasets[0]['jets'].dtype,
 data = datasets[0]['jets'])

	emtopo_file.create_dataset('super_tracks',
 shape = datasets[0]['super_tracks'].shape,
 dtype = datasets[0]['super_tracks'].dtype,
 data = datasets[0]['super_tracks'])

	#sanity check the shapes of the h5 files
	print(datasets[0].keys)
	print(emtopo_file.keys)


	input.close()
	emtopo_file.close()
