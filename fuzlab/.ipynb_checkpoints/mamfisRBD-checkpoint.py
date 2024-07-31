from fuzlab.FuzzyInferenceSystem import FuzzyInferenceSystem
import numpy as np

class mamfisRBD(FuzzyInferenceSystem):
    def __init__(self, 
        Name                    = 'fis',
        AndMethod               = 'min',
        OrMethod                = 'max',
        ImplicationMethod       = 'min',
        AggregationMethod       = 'max',
        DefuzzificationMethod   = 'centroid',
        WablOptimism            = 0.5, 
        WablDegrees             = 21,
        WablImportances         = np.ones(21)):

        FuzzyInferenceSystem.__init__(self)

        self.Name                       = Name
        self.Type                       = 'mamdaniRBD'
        self.AndMethod                  = AndMethod
        self.OrMethod                   = OrMethod
        self.ImplicationMethod          = ImplicationMethod
        self.AggregationMethod          = AggregationMethod
        self.DefuzzificationMethod      = DefuzzificationMethod
        self.WablOptimism               = WablOptimism
        self.WablDegrees                = WablDegrees
        self.WablImportances            = WablImportances
    