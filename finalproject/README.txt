Daniel Alabi
Cody Wang
CS 324

Regularized SVD (Singular Value Decomposition) 
==============================================
Our project was to implement and analyze regularized SVD in python, 
as suggested by Simon Funk and others [1,2].

For a more detailed explanation of the regularized SVD technique we use 
and also some analysis, see our paper, finalprojectpaper.pdf.

1) We have 7 main python files:
i) regularizedSVD.py - contains implementation of SvdMatrix
   that reads in ratings and trains the UV matrices based on these
   ratings. Reports the final train RMSE.
   Can also read in test ratings and report the final test RMSE.
ii) plotsSVD.py - used to plot graphs used to pick the best
    parameters.
iii) writeplots.py - used to write results of varying different
    parameters used in our SvdMatrix class to a file. 
    !!WARNING!!:This one runs very slow because it tests using three
    sets of different parameters.
iv) userbased.py - contains implementation of user-based
     collaborative filtering technique. This is used as a control.
     We compare how good/bad our technique is against this.
v) itembased.py - contains implementation of item-based
   collaborative filtering technique. Also used as a control.
vi) shared.py - contains shared code necessary for collaborative filtering
    techniques to run.
vii) scipySVDcontrol.py - contains implementation of SVD technique
    using scipy SVD, filling in the partial utility matrices with
    averages.

2) All the plot files generated are included in graphs folder
and are named *.png.

3) All the data files generated for plotting in writeplots.py
are placed in the data folder.

4) Datasets are not included but can be downloaded from 
http://www.grouplens.org/node/73. We used "ua.base" and "ua.test" from
the 100K dataset, and "ratings.dat" from the 1M dataset.


See the contents of the above files for more information on how to
run them.

[1] http://www.timelydevelopment.com/demos/NetflixPrize.aspx
[2] http://sifter.org/~simon/Journal/20061211.html

