'''

Author  : Kamalakar Kududhula
version : python 2.7

Problem link https://www.hackerrank.com/challenges/nested-list/problem


Given the names and grades for each student in a Physics class of N students, 
store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade. 
If there are multiple students with the same grade, order their names alphabetically and print each name on a new line. 

Note: 
Input Format 
The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line 
contains their grade. 
Constraints 
There will always be one or more students having the second lowest grade. 
Output Format 
Print the name(s) of any student(s) having the second lowest grade in Physics; 
if there are multiple students, order their names 
alphabetically and print each one on a new line. 

Sample Input 
5 
Harry 
37.21 
Berry 
37.21 
Ti na 
37.2 
Akriti 
41 
Harsh 
39 

Sample Output 
Berry 
Harry 

Explanation 
There are 5 students in this class whose names and grades are assembled to build the following list: 
python students = ['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2) ['Akriti', 41] , ['Harsh', 39]] 
The lowest grade of 37.2 belongs to Tina. 
The second lowest grade of 37.21 belongs to both Harry and Berry, 
so we order their 
names alphabetically and print each name on a new line. 


'''


lists = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    lists.append([name,score])
    
second_low_grade = sorted(set([score for name,score in lists])[1]
print ("\n".join(sorted([name for name,score in lists if score == second_low_grade])))
