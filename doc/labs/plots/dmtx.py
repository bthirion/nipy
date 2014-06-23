from numpy import array
from nipy.modalities.fmri.design_matrix import make_dmtx
from nipy.modalities.fmri.experimental_paradigm import EventRelatedParadigm
# Specify an event-related paradigm
conditions = ['smile', 'smile', 'listen', 'listen', 'read', 'read']
onsets = [30, 70, 10, 90, 40, 60] # onset time in s.
paradigm = EventRelatedParadigm(conditions, onsets)
# provide frametimes and compute the design matrix
frametimes = array(range(0, 100)) # time of the scans
X = make_dmtx(frametimes, paradigm, drift_model='polynomial', drift_order=3)
X.show()
