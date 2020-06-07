# Determining Litho Boundaries from gamma logs
## Transform2020- Geology and Python conference

This is some data and ideas for a hackathon project called [t20-litho_boundary_from_gamma](https://swung.slack.com/archives/C014YJM3UJW) taking place at the [Transform 2020](https://transform2020.sched.com/)  conference, a fully online geoscience conference.  This repo is to provide a dataset for this project.

### What are we trying to do?

Estimate lithology boundaries from downhole geophysics, using a continuous wavelet tesselation algorithm (CWT).  Only boundaries at this stage, not lithological values.

A dataset for one hole can be found in the folder. Following are some basic instructions to play with.

1. Try and get some code to make lithology boundaries based (CWT) algorithm that read the gamma data in and outputs the interval boundaries.
2. Next step would be to view the gamma log, with the associated litho data and the outputted tesselations.  Essentially 3 strips.
3. Somehow to compare the the tesselation boundaries with the actual lithology boundaries.  What can we use to compare?
4. Repeat until the a reasonable match is found.  I think the trick here is dialling in the right.
5. When we get some results, maybe even plot using DASH or something flash like that.
