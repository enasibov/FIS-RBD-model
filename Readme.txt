""" 
"fuzlab" is a package extending the FuzzyLab library (https://github.com/ITTcs/fuzzylab) 
for constructing Fuzzy Inference Systems (FIS) such as: 
	- Mamdani type FIS - the classical Mamdani type FIS, 
	- Mamdani type FIS with Rule Based Defuzzification (FIS-RBD), 
	- Sugeno type FIS.

The "fuzlab" package contains defuzzification methods such as: 
	- "wabl" - the weighted average based on levels,
	- "centroid" - the centroid of gravity (COG) method,
	- "mom" - the mean of maxima,
	- "som" - the smallest of maxima,
	- "lom - the largest of maxima.

The "fuzlab" package extends the existing Fuzzylab library with the following modified/inserted modules:
	- "defuzz.py" with "wabl" defuzzification extencion,
	- "evalfis.py" with "mamdaniRBD" model extencion,
	- "FuzzyInferenceSystem" with parameters: 
		"WablOptimizm" (optimism parameter for WABL),
        	"WablDegrees" (number of discrete level sets for WABL),
		"WablImportances" (weights of level sets for WABL). 
	- "mamfisRBD.py", a newly designed class for constructind the FIS-RBD model,


The "test.ipynb" notebook file contains usage examples of "fuzlab" package with different FIS modules.

""" 


