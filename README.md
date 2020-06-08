# Determining Litho Boundaries from gamma logs
## Transform2020- Geology and Python conference

This is some data and ideas for a hackathon project called [t20-litho_boundary_from_gamma](https://swung.slack.com/archives/C014YJM3UJW) taking place at the [Transform 2020](https://transform2020.sched.com/)  conference, a fully online geoscience conference.  This repo is to provide a dataset for this project.

### What are we trying to do?

Estimate lithology boundaries from downhole geophysics, using a continuous wavelet tesselation algorithm (CWT).  Only boundaries at this stage, not lithological values.  Idea was to use an existing packages, found [PyWavelets](https://pywavelets.readthedocs.io/en/latest/index.html#) which may or may not do the job.  Based on a paper by Evelyn Jun Hill ([here](https://www.researchgate.net/publication/339871641_Improving_Automated_Geological_Logging_of_Drill_Holes_by_Incorporating_Multiscale_Spatial_Methods)) the CWT family bestsuited for this kind of work is Gassian, which needs to be used in the algorithm.

A dataset for one hole can be found in the folder. Following are some basic instructions to play with.

### Suggested workflow
1. Try and get some code to make lithology boundaries based (CWT) algorithm that read the gamma data in and outputs the interval boundaries.  Trying to use the code snippet on the home page of hte PyWavelets package with a 'gaus'
2. Next step would be to view the gamma log, with the associated litho data and the outputted tesselations.  Essentially 3 strips.
3. Somehow to compare the the tesselation boundaries with the actual lithology boundaries.  What can we use to compare?
4. Repeat until the a reasonable match is found.  I think the trick here is dialling in the right.
5. When we get some results, maybe even plot using DASH or something flash like that.

### Where are we up to?
Stuck on step 1.  fixed!
Added more data to repo folder, three holes now instead of 1 and added short spaced density(DENB), caliper(CADE) and sonic(MC2F) logs to the dataset.
Got code working to generate a plot.  Yay!

Now trying to ..
-generate a strength of boundary defn plot
-include a lithology log  in the plot
-genererate a mosiac plot



