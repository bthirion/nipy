General linear Model
====================

.. currentmodule:: nipy.modalities.fmri.glm.py

General Linear Model fitting consists then in estimating the brain
responses associated with the columns of design matrix. The fit
consists in a weighted least-square fit to esti- mate the model
parameters and a variance-covariance matrix parametrized by two
parameters: the amount of noise vari- ance in the voxel time course
and the lag-1 autocorrelation of the noise Bullmore et al. (1996). The
model and covari- ance parameters are estimated in an alternate
optimization scheme. The corresponding interface is relatively simple,
as the user simply needs to provide the design matrix and the data
matrix. It yields a class that contains summary statis- tics
(estimated effects and their covariance matrix) that can be used for
further investigation; the standard way of exploiting this output
consists in specifying a linear combination of the regressors and test
the significance in signed (t-) or unsigned (F-test) The simplicity of
the illustrated in the following listing.

.. plot:: labs/plots/glm.py
    :include-source:



