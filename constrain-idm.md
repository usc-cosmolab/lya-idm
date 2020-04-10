# Constrain IDM interaction strength using ly-alpha data

1. Create a new conda environment for this project, e.g.,
	
	```
	conda create -n idm numpy scipy matplotlib jupyterlab cython
	```
	
	This is because you will be installing a new version of CLASS that you don't want to mix up with any version of class in any other environment. 
	
2. Clone and install the version of the CLASS code that implements IDM (but call it something different from the original CLASS repo):

	```
	git clone https://github.com/kboddy/class_public class_idm
	cd class_idm
	git checkout dmeff
	make
	```
	
3. Verify that you can call classy with IDM parameters (e.g., passing a dictionary including IDM params to `lya.theory.get_theory_pk()`.

4. Write a function that returns the log-likelihood of the lyman-alhpa data given a chosen dark matter mass and cross-section (all other cosmological parameters fixed to the values in `lya.conf.lcdm_params`).  

5. For a chosen fixed mass, evaluate this likelihood at a range of cross-section values to map out a 1-d likelihood (you will need to explore what a sensible range of values should be).  Make a plot of log-likelihood vs. cross-section.

6. From this analysis, find the cross-section that represents the 95% upper limit.

7. Repeat steps 5-6 for a few different fixed masses.