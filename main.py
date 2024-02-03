# Inbar Lev Tov 316327246

import matplotlib.pyplot as plt
import numpy as np
import random

if __name__ == '__main__':
    # initial settings for graph1
    graph = plt.figure()
    axes = plt.axes(projection = '3d')
    farView = -100
    closeView = 100
    axes.set_xlim([closeView, farView])
    axes.set_ylim([closeView, farView])
    axes.set_zlim([closeView, farView])
    axes.set_xlabel('x', color='blue')
    axes.set_ylabel('y', color='blue')
    axes.set_zlabel('z', color='blue')

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
        axes.plot([origin[0], randomX[i]], [origin[1], randomY[i]], [origin[2], randomZ[i]], c = 'b')
        axes.scatter(originalPoints[i][0], originalPoints[i][1], originalPoints[i][2], c='r', s=amount)

    # creating a transformation matrix that includes rotation & translation
    parameters = []
    for i in range(0, 6):
        parameters.append(random.random())
    #matrix = [parameters[0], (-1 * parameters[1]), parameters[2], parameters[3], parameters[4], (-1 * parameters[5]), 0, 0, 1]
    matrix = [0, 1, 2, 1, 0, 3, 0, 0, 1]
    matrix = np.reshape(matrix, (3, 3))
    newPoints = []
    for i in range(0, amount):
        newP = np.dot(matrix, originalPoints[i])
        newPoints.append([newP[0], newP[1], newP[2]])
        axes.plot([origin[0], newP[0]], [origin[1], newP[1]], [origin[2], newP[2]], c='g')
        axes.scatter(newP[0], newP[1], newP[2], c='r', s=amount)

    # showing graph
    axes.view_init(elev=22, azim=-155, roll=0)
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





