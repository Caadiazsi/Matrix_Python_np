import numpy as np
from time import time;


for s in range (1, 10):
	size = s*50
	matrixA = np.array((size,size))
	matrixB = np.array((size,size))
	matrixAxB = np.array((size,size))
	Operations = size*size*((2*size)-1)
	print ("Size: ", size)
	print ("Operations: ", Operations)
	matrixA.fill(1);
	matrixB.fill(2);
	matrixAxB.fill(0);
	initial_Time = time();
	for times in range (0, 10):
		matrixAxB = np.dot(matrixA, matrixB)
	execution_Time = time() - initial_Time;
	print ('Execution_Time: ', execution_Time/(Operations*10000))
	print ('------------------------')