N = int(input())
'''
Use map function to map the print function to eahc of the iterable element when python detects the s variable, it will automatically perform print function...
This is a really interesting discovery, to print something without actually print something...
Almost forgot, this doesn't work in Python2 because of the print function inside a map funciton, map returns a generator
'''
s = list(map(lambda fuck:print(fuck,end=""),range(1,N+1)))
