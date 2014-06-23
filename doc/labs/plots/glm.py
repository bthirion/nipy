from nipy.labs.utils.simul_multisubject_fmri_dataset import \
     surrogate_4d_dataset
from nipy.modalities.fmri.glm import FMRILinearModel
shape = (10, 10, 10) # simulate a cubic image
n_scans = 100 # equal to the number of frametimes
fmri_data = surrogate_4d_dataset(shape=shape, n_scans=n_scans)
# run the GLM
my_glm = FMRILinearModel(fmri_data, X.matrix)
# GLM fitting
my_glm.fit(do_scaling=True, model='ar1')
listen_vs_read = array([1, -1, 0, 0, 0, 0, 0])
z_map, = my_glm.contrast(listen_vs_read)
