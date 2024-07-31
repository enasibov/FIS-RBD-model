from fuzlab.FuzzyInferenceSystem import FuzzyInferenceSystem
import numpy as np

class mamfis(FuzzyInferenceSystem):
    def __init__(self, 
        Name                    = 'fis',
        AndMethod               = 'min',
        OrMethod                = 'max',
        ImplicationMethod       = 'min',
        AggregationMethod       = 'max',
        DefuzzificationMethod   = 'centroid',
        WablOptimism            = 0.5,  # optimism parameter for WABL
        WablDegrees             = 21,   # number of discrete level sets for WABL
        WablImportances         = np.ones(21)): # weights of level sets for WABL. 

        FuzzyInferenceSystem.__init__(self)

        self.Name                       = Name
        self.Type                       = 'mamdani'
        self.AndMethod                  = AndMethod
        self.OrMethod                   = OrMethod
        self.ImplicationMethod          = ImplicationMethod
        self.AggregationMethod          = AggregationMethod
        self.DefuzzificationMethod      = DefuzzificationMethod
        self.WablOptimism               = WablOptimism
        self.WablDegrees                = WablDegrees
        self.WablImportances            = WablImportances
    