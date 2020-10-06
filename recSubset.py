s = "abc"
subsets = set()

def recSubset(l):
    if not l:
        return
    print(l)
    subsets.add(l)
    recSubset(l[1:])
    recSubset(l[:-1])

# if __name__ == '__main__':
#     recSubset(s)
#     print(subsets)

# Python3 program to generate power set
def powerSet(string , index , curr):

	# string : Stores input string
	# curr : Stores current subset
	# index : Index in current subset, curr
	print(string,index,curr)
	if index == len(string):
		subsets.add(curr)
		return

	powerSet(string, index + 1,
			curr + string[index])
	powerSet(string, index + 1, curr)

# Driver Code
if __name__ == "__main__":

	s1 = "abc"
	index = 0
	curr = ""
	powerSet(s1, index , curr)

# This code is contributed by Ekta Singh
