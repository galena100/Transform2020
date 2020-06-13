# Determining Litho Boundaries from gamma logs for coal mining geoscientists
## Transform2020- Geology and Python conference

<img src="https://raw.githubusercontent.com/galena100/Transform2020/master/t20-litho_boundary_from_gamma/test_on_synthetic_data.JPG" alt="Your image title" width="500"/>

This is some data and ideas for a hackathon project called [t20-litho_boundary_from_gamma](https://swung.slack.com/archives/C014YJM3UJW) taking place at the [Transform 2020](https://transform2020.sched.com/)  conference, a fully online geoscience conference.  This repo is to provide a dataset for this project.

### What are we trying to do?

Estimate lithology boundaries from downhole geophysics GR log, using a continuous wavelet transform algorithm (CWT).  Idea was to use an existing packages, found [PyWavelets](https://pywavelets.readthedocs.io/en/latest/index.html#).  Based on a paper by Evelyn Jun Hill ([here](https://www.researchgate.net/publication/339871641_Improving_Automated_Geological_Logging_of_Drill_Holes_by_Incorporating_Multiscale_Spatial_Methods)) the CWT family best suited for this kind of work is Gaussian and its derivative, which needs to be used in the algorithm.

A dataset for one hole and one curve (or three holes with four curves) can be found in the folder. Following is a basic strategy  to play with.

### Suggested workflow
1. Try and get some code to make lithology boundaries based (CWT) algorithm that read the gamma data in and outputs the interval boundaries.  Trying to use the code snippet on the home page of the PyWavelets package with 'gaus2'
2. Next step would be to view the gamma log, with the associated litho data and the outputted tesselations.  Essentially 3 strips.
3. compare the the tesselation boundaries with the actual lithology boundaries.  
4. Repeat until the a reasonable match is found.  I think the trick here is dialling in the right.
5. When we get some results, maybe even plot using DASH or something flash like that.

### Where are we up to?

- [x] conditioning the data
    
- [x] define the boundary using CWT
    
- [x] boundary strength calculation
    
- [x] include a lithology log in the plot 
    
- [x] genererate a mosaic plot (kind of solved?)
