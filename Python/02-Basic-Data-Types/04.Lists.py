'''
Author  : Kamalakar Kududhula
version : python 2.0

Problem link https://www.hackerrank.com/challenges/python-lists/problem



Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command 
will be of the  types listed above. Iterate through each command in order and perform the corresponding 
operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line i of the N subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(raw_input())
    list = []
    for i in range(N):
        i = raw_input().split()
        if i[0] != 'print':
            cmd = i[0]
            args = i[1:]
            # map(int,args) converts the string elements in list to integer, and tuple converts it to a tuple
            eval("list.{0}{1}".format(cmd,tuple(map(int,args))))
        else:
            print list


    # OLD Method or for beginners
    '''

    N = int(raw_input())
    list = []
    for i in range(N):
        i = raw_input().split(" ")
        print i
        if i[0] == 'append':
            list.append(int(i[1]))
        if i[0] == 'insert':
            list.insert(int(i[1]),int(i[2]))          
        if i[0] == 'remove':
            list.remove(int(i[1]))
        if i[0] == 'pop' and len(list) != 0:
            list.pop()
        if i[0] == 'sort':
            list.sort()
        if i[0] == 'reverse':
            list.reverse()
        if i[0] == 'print':
            print list
      '''