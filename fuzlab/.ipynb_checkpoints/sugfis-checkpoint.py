from fuzlab.FuzzyInferenceSystem import FuzzyInferenceSystem
import numpy as np

class sugfis(FuzzyInferenceSystem):
    def __init__(self, 
        Name                    = 'fis',
        AndMethod               = 'prod',
        OrMethod                = 'probor',
        ImplicationMethod       = 'prod',
        AggregationMethod       = 'sum',
        DefuzzificationMethod   = 'wtaver'):

        FuzzyInferenceSystem.__init__(self)

        self.Name                       = Name
        self.Type                       = 'sugeno'
        self.AndMethod                  = AndMethod
        self.OrMethod                   = OrMethod
        self.ImplicationMethod          = ImplicationMethod
        self.AggregationMethod          = AggregationMethod
        self.DefuzzificationMethod      = DefuzzificationMethod
        
    