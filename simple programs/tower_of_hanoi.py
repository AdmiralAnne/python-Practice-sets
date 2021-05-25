""" The tower of hanoi is a puzzle invented by French mathematician Édouard Lucas.
	The initial set-up and the rules are simple. We are given three pegs, 
	one of them has 8 discs in stacked in decreasing order of 
	of their size from bottom to top. 
	Our goal is to move all of the discs to another peg with the restrictions that:
	a) We can only move one disc at a time and 
	b) That a larger disc cannot be stacked on top of a smaller disc.
	Another more interesting version of this puzzle as stated in the book Concrete Mathematics goes as under

	" Lucas [208] furnished his toy with a romantic legend about a much larger
	Tower of Brahma, which supposedly has 64 disks of pure gold resting on three
	diamond needles. At the beginning of time, he said, God placed these golden
	disks on the first needle and ordained that a group of priests should transfer
	them to the third, according to the rules above. The priests reportedly work
	day and night at their task. When they finish, the Tower will crumble and
	the world will end "


	This problem can be solved with simple recursion as shown under. I encourage you to try out this program and find the
	number of moves that the priests can make before the tower crumbles and the world ends.   
""" 


def numberOfMoves(n):
	if(n==0):
		return 0
	elif(n==1):
		return 1
	else:
		return 2*numberOfMoves(n-1)+1
#main
numberOfDiscs = int(input("Enter number of discs :"))
result = numberOfMoves(numberOfDiscs)
print("Number of moves required: ",result) 
