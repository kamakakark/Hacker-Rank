'''

Problem link https://www.hackerrank.com/challenges/list-comprehensions/problem

List Comprehensions
Let's learn about list comprehensions! You are given three integers X, Y and Z representing the
dimensions of a cuboid along with an integer N. You have to print a list of all possible coordinates given (i,j,k)
by on a 3D grid where the sum of i+j+k is not equal to N. Here,
Input Format
Four integers X,Y,Z and N each on four separate lines, respectively.
Constraints
Print the list in lexicographic increasing order.
Sample Input 0
1
1
1
2
Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

'''

if __name__ == '__main__':
    #x = int(raw_input())
    #y = int(raw_input())
    #z = int(raw_input())
    #n = int(raw_input())

    x,y,z,n = [int(input()) for i in range(4)]
    print [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]