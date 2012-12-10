#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Example of a one-sample t-test using a mixed-effect model.
This script takes individual contrast images, variances and masks and 
runs a simple one-sample mixed effects test.
This can be readily generalized to any design matrix.

This particular example shows the statical map of a contrast
related to a computation task
(subtraction of computation task minus sentence reading/listening).

Needs matplotlib.

Author : Bertrand Thirion, 2012
"""
print __doc__

#autoindent
from os import mkdir, getcwd, path

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise RuntimeError("This script needs the matplotlib library")

from nibabel import load, concat_images, save, Nifti1Image

from nipy.algorithms.statistics.mixed_effects_stat import one_sample_ttest
from nipy.labs.mask import intersect_masks
from nipy.modalities.fmri.glm import FMRILinearModel
from nipy.labs.viz import plot_map, cm

# Local import
from get_data_light import DATA_DIR, get_second_level_dataset

# Get the data
n_subjects = 12
n_beta = 29
data_dir = path.join(DATA_DIR, 'group_t_images')
mask_images = [path.join(data_dir, 'mask_subj%02d.nii' % n)
               for n in range(n_subjects)]
betas = [path.join(data_dir, 'con_%04d_subj_%02d.nii' % (n_beta, n))
         for n in range(n_subjects)]
spms = [path.join(data_dir, 'spmT_%04d_subj_%02d.nii' % (n_beta, n))
         for n in range(n_subjects)]

missing_files = np.array([not path.exists(m) for m in 
                          mask_images + betas + spms])
if missing_files.any():
    get_second_level_dataset()

write_dir = path.join(getcwd(), 'results')
if not path.exists(write_dir):
    mkdir(write_dir)

# Compute a population-level mask as the intersection of individual masks
mask = intersect_masks(mask_images)
grp_mask = Nifti1Image(mask.astype(np.int8), load(mask_images[0]).get_affine())

def get_effects_and_variance(betas, spms, mask):
    """Read the data and provide effects and variance arrays"""
    effect = np.zeros((mask.sum(), len(betas)))
    variance  = np.zeros((mask.sum(), len(betas)))
    for i, (beta, spm) in enumerate(zip (betas, spms)):
        effect[:, i] = load(beta).get_data()[mask]
        variance[:, i] = (effect.T[i] ** 2  /(
                          1.e-10 + load(spm).get_data()[mask] ** 2))
    effect[np.isnan(effect)] = 0
    variance[np.isnan(variance)] = 1.e10
    return effect, variance

effect, variance = get_effects_and_variance(betas, spms, mask)
t_mfx = one_sample_ttest(effect.T, variance.T)
write_t = mask.astype(np.float)
write_t[mask] = t_mfx

# write the results
affine = load(mask_images[0]).get_affine()
save(Nifti1Image(write_t, affine), path.join(write_dir, 'one_sample_z_map.nii'))

# look at the result
vmax = max(- write_t.min(), write_t.max())
vmin = - vmax
plot_map(write_t, affine,
         cmap=cm.cold_hot,
         vmin=vmin,
         vmax=vmax,
         threshold=3.,
         black_bg=True)
plt.savefig(path.join(write_dir, '%s_z_map.png' % 'one_sample'))
plt.show()
print "Wrote all the results in directory %s" % write_dir

