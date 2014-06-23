Design matrix
=============

.. currentmodule:: nipy.modalities.fmri.design_matrix.py

FMRI data analysis relies on the modeling of temporal effects that
represent the expected impact of the experimental events on the brain
signals, plus a set of confounds.

Neuroimagers typically have to make a set of choices here: for
instance, they need to decide which model of the hemodynamic response
function (hrf) they want to use to model evoked response. 

The hrf is a low-pass filter that delays some input signal --an
idealized model of neural responses-- with the observed Blood
Oxygen-Level Dependent (BOLD) contrast.

Different parametrization of this filter have been proposed in the
literature \cite{Friston1998,Glover1999}; moreover, it is often
advised to include the first derivative of the chosen model to account
for unpredictable delays in the response, that can be due to local
vasculature differences, uncertainty on the exact neural response
timing, or shortcomings of the slice timing correction.

Similarly, several different parametrizations can be used to model
signals of no interest, such as low-frequency drifts.

In practice, it is advised to consider different parametrizations of
the expected responses.
 
In terms of software design, this means that as simple yet flexible
interface is needed for model specification

.. plot:: labs/plots/dmtx.py
    :include-source:


**Reference**: 
Glover, G. H. Neuroimage, 9(4), (1999) 416--429. 
Friston, K. J., et al. Magn Reson Med, 39(1), (1998) 41--52.


