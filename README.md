minefinal
=========

Big Goal: to make predictions on our movielens dataset using
      Regularized SVD
Smaller:
--------
* Make program that emulates Gradient-Descent UV decomposition
   suggested by Simon Funk.
   Run on dataset. Make predictions.
   Measure accuracy/speed.
   
* Make program using Scipy "normal" SVD decomposition. Fill
   missing values with averages.

* Compare contrast results/approaches.


Paper: Funk SVD Method
======================
* State the problem: Rank-k approximation. Why useful? How?
   
*  Intro.: Current approaches. Problems with current approaches.
   SVD approach? Not scalable.
   New method: Simon Funk's approach.
   How we decided to call it "Regularized Gradient-Descent SVD".
   Why regularized? Why Gradient-Descent?
   How we understood the article.
   How we dug deep into the article. 
   What other articles told us about Simon Funk's approach.

*  Experimental setup: RMSE calculation as a prediction. Why?

*  Talk about our program: how it works? How it does what it does?
   Refer heavily to Simon Funk's method.

*  Talk about what other programs we implemented to test again
   our new approach:
   i) Test against recommendation sytem.
   continual averages until RMSE under certain threshold
   Why did we decide to use these methods as controls?

*  Present results:
   RMSE comparison for 3 methods for different k.
   Time comparison for 3 methods for different k.
   
* Conclusion:
   What have you found so far using the movie dataset.



