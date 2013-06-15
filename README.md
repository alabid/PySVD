Daniel Alabi
Cody Wang
CS 324

Regularized SVD (Singular Value Decomposition) 
==============================================
Our project was to implement and analyze regularized SVD in python, 
as suggested by Simon Funk and others [1,2].

For a more detailed explanation of the regularized SVD technique we use 
and also some analysis, see our paper, finalproject.pdf.

We have 5 main python files:
i) regularizedSVD.py - contains implementation of SvdMatrix
   that reads in ratings and trains the UV matrices based on these
   ratings. Reports the final train RMSE.
   Can also read in test ratings and report the final test RMSE.
ii) plotsSVD.py - used to plot graphs used to pick the best
    parameters.
iii) writeplots.py - used to write results of varying different
    parameters used in our SvdMatrix class to a file.
iv) userbased.py - contains implementation of user-based
     collaborative filtering technique. This is used as a control.
     We compare how good/bad our technique is against this.
v) itembased.py - contains implementation of item-based
   collaborative filtering technique. Also used as a control.
vi) scipySVDcontrol.py - contains implementation of SVD technique
    using scipy SVD, filling in the partial utility matrices with
    averages.

See the contents of the above files for more information on how to
run them.

[1] http://www.timelydevelopment.com/demos/NetflixPrize.aspx
[2] http://sifter.org/~simon/Journal/20061211.html

