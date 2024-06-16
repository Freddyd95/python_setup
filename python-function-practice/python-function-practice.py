#def max_num(a, b,c):
    #return max([a,b,c])

#print(max_num(1,2,3))
#print(max_num(150,70,1))
#print(max_num(20,45,2))

#def mult_list():
    #if len(1) == 0:
     #   return 0
    #prod = 1[0] > 1
    #for i in 1[1:]:
     #   prod = prod * i
      #  return prod

#print(mult_list([1,2,3]))
#print(mult_list([]))
#print(mult_list([15]))
    
#def rev_string(string):
 #   return string[::-1]
#print(rev_string(""))
#print(rev_string("bone"))
#print(rev_string("string"))

#def num_within(x,a,b):
 #   return x in range(a,b+1)

#print(num_within(4,6,1))
#print(num_within(6,2,6))
#print(num_within(17,2,10))

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]

      length = len(row_prev)+1
      for i in range(length):
       
        if i == 0:
          row.append(1)
       
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    
    for row in triangle:
      print(row)

pascal(2)
pascal(5)
