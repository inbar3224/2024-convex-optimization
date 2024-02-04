# 2024-convex-optimization

Student Name: Inbar Lev Tov

Student ID: 316327246

## first step:
- I positioned the origin (the camera) on the far side of the screen.
- I randomly sampled 5 red points in a 3D coordination system and connected the blue vectors from the camera to those points.
- I then went on to manually create a transformation matrix that consists of only rotation and translation (no scaling required).
- The matrix I created rotate the points by 20 degrees and move them by 2 on the x axes and by 3 on the y axes.

![/images/transformation_matrix](/images/transformation_matrix.png)

- I multiplied the original points and received new red points with new vectors attached to them from the camera (green ones).

![/images/graph_for_first_step1](/images/graph_for_first_step1.png)

- I calculated the inverse transformation matrix and multiplied the new points with it in order to get the original points back.

![/images/results_for_first_step1](/images/results_for_first_step1.png)

- Here the transformation matrix was fairly simple and the sampling size (only 5 points) was fairly small - so the cost we might have received by those changes is 0.
- With a larger sample or alternatively an "uglier" transformation matrix we would receive some cost and not manage to return to the same original points.

The next step would be looking at a larger sample and trying to minimize the cost.