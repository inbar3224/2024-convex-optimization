# Inbar Lev Tov 316327246

import matplotlib.pyplot as plt
import numpy as np
import random

if __name__ == '__main__':
    # initial settings for graph and axes
    graph, axes = plt.subplots(1,2, subplot_kw = dict(projection = '3d'))
    farView = -100
    closeView = 100
    axes[0].set_title('Original Points')
    axes[1].set_title('New Points')
    for i in range(0, 2):
        axes[i].set_xlim([closeView, farView])
        axes[i].set_ylim([closeView, farView])
        axes[i].set_zlim([closeView, farView])
        axes[i].set_xlabel('x', color='blue')
        axes[i].set_ylabel('y', color='blue')
        axes[i].set_zlabel('z', color='blue')
        axes[i].view_init(elev=16, azim=-127, roll=0)

    # defining origin
    origin = [farView, farView, farView]

    # randomly selecting n initial points in 3D
    amount = 5
    lowLimit = int(farView * 0.8)
    highLimit = int(closeView * 0.8)
    randomX = random.sample(range(lowLimit, highLimit), amount)
    randomY = random.sample(range(lowLimit, highLimit), amount)
    randomZ = random.sample(range(lowLimit, highLimit), amount)
    originalPoints = []
    for i in range(0, amount):
        originalPoints.append([randomX[i], randomY[i], randomZ[i]])
        axes[0].plot([origin[0], randomX[i]], [origin[1], randomY[i]], [origin[2], randomZ[i]], c = 'b')
        axes[0].scatter(originalPoints[i][0], originalPoints[i][1], originalPoints[i][2], c='r', s=amount)

    # creating a transformation matrix that includes rotation & translation
    matrix = [0.408, -0.342, 2, 0.342, 0.408, 3, 0, 0, 1]
    matrix = np.reshape(matrix, (3, 3))
    newPoints = []
    for i in range(0, amount):
        newP = np.dot(matrix, originalPoints[i])
        newPoints.append([newP[0], newP[1], newP[2]])
        axes[1].plot([origin[0], newP[0]], [origin[1], newP[1]], [origin[2], newP[2]], c='g')
        axes[1].scatter(newP[0], newP[1], newP[2], c='r', s=amount)

    # showing graph
    plt.show()

    # find inverse matrix
    inverseM = np.linalg.inv(matrix)
    finalPoints = []
    for i in range(0, amount):
        newP = np.dot(inverseM, newPoints[i])
        finalPoints.append([newP[0], newP[1], newP[2]])

    # reshaping the data into matrices form and printing results
    originalPoints = np.reshape(np.array(originalPoints), (amount, 3))
    newPoints = np.reshape(np.array(newPoints), (amount, 3))
    finalPoints = np.reshape(np.array(finalPoints), (amount, 3))

    print("the original points:")
    print(originalPoints)
    print("the new points after multiplying the transformation matrix")
    print(newPoints)
    print("the final points after multiplying the inverse transformation matrix")
    print(finalPoints)