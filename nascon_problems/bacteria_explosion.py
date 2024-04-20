inp = input() # take input for number of rows and the number of cycles
rows, cycles = int(inp.split()[0]), int(inp.split()[1]) #separates the rows and cycles
matrix = [] #declare your matrix as a list

for i in range (rows): #run the input loop for number of rows
    row = input() #take the input as a string
    elements = row.split() #this splits the input string based of spaces and saves it in a list
    matrix.append( [int(elem) for elem in elements]) #this typecasts the elements from string to ints an also appends the matrix with this new row (a list)
print(f"input matrix: {matrix} \n cycles: {cycles}\n") #prints the matrix
# rows = input_str.strip().split('\n') this may be used if you get a multiline input to separate the inputs into rows

if (cycles==1):
    displacement =1 #handle special case
else:
    displacement = cycles/2                     #formula to find disp from cycle
    if displacement.is_integer():               #
        displacement = -int(displacement)       #
    else:                                       #
        displacement = int(displacement)+1      #get the value for displacement from cycles
print(f"displacement : {displacement}\n")

cols = len(elements) #get number or cols
matrix = [elem for row in matrix for elem in row] #flatten the matrix
newMatrix= [0 for _ in range(rows*cols)] #initialize same sized matrix with zeros

for i in range (rows*cols):
    new_i = (i+displacement)%(rows*cols) #apply displacement on flat matrix
    newMatrix[new_i]= matrix[i]          #

reshaped_matrix = []                    #reshaping the flat matrix
index=0                                 #
for _ in range(rows):                   #
    rowN = newMatrix[index:index+cols]  #
    reshaped_matrix.append(rowN)
    index += cols
print(f"matrix before explosion: {reshaped_matrix}\n")

exit_matrix =[]
for i in range(rows*cols):
    exit_matrix.append(sum(newMatrix) - newMatrix[i]) #implying explosion logic

reshaped_exploded_matrix = []                    #reshaping the flat matrix
indexN=0                                 
for _ in range(rows):                   
    rowN = exit_matrix[indexN:indexN+cols]  
    reshaped_exploded_matrix.append(rowN)
    indexN += cols
print(f"final matrix{reshaped_exploded_matrix}")