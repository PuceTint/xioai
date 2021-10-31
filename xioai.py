import numpy as np

def nextMoveSet(currentMove):
	movesample=np.array([])
	ans=[]
	for row in range(3):
		for col in range(3):
			if not currentMove[row,col]:

				movesample=np.copy(currentMove)
				movesample[row,col]=1
				if not (
				abs(sum(movesample[row,:])==3) 
				or abs(sum(movesample[:,col])==3)
				or abs(sum(movesample[q,q] for q in range(3)))==3
				or abs(sum(movesample[q,2-q] for q in range(3)))==3		
				):
					print(movesample,"\n")
					ans.append(movesample)


				movesample=np.copy(currentMove)
				movesample[row,col]=-1
				if not (
				abs(sum(movesample[row,:])==3) 
				or abs(sum(movesample[:,col])==3)
				or abs(sum(movesample[q,q] for q in range(3)))==3
				or abs(sum(movesample[q,2-q] for q in range(3)))==3		
				):
					print(movesample,"\n")
					ans.append(movesample)

	return ans

def chooseMove(currentMove):
	pass
				
			
plane = np.array([[1,1,1],[0,0,1],[-1,-1,0]])
#xio game, 1 = x, -1 = o
nextMoveSet(plane)