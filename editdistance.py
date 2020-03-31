class EditDistance():

  def __init__(self):
    """
    Do not change this
    """

  def calculateLevenshteinDistance(self, str1, str2):
            n = len(str1) #col
            m = len(str2) #row
            matrix = [[-1 for col in range(m+1)] for row in range(n+1)]
            matrix[0][0]=0
            for i in range(1,n+1):
                matrix[i][0] = matrix[i-1][0] + 1

            for j in range(1,m+1):
                matrix[0][j] = matrix[0][j-1] + 1

            for i in range(1,n+1):
                for j in range(1,m+1):
                    if str1[i-1] == str2[j-1]:
                        subCost = 0
                    else:
                        subCost = 1
                    matrix[i][j] = min(matrix[i-1][j]+1,matrix[i-1][j-1]+subCost,matrix[i][j-1] + 1)
            return matrix[n][m]

  def calculateOSADistance(self, str1, str2):
            n = len(str1) #col
            m = len(str2) #row
            if n == 0: return m
            if m == 0: return n
            matrix = [[0 for col in range(m+1)] for row in range(n+1)]
            matrix[0][0]=0
            for i in range(1,n+1):
                matrix[i][0] = matrix[i-1][0] + 1

            for j in range(1,m+1):
                matrix[0][j] = matrix[0][j-1] + 1

            for i in range(1,n+1):
                for j in range(1,m+1):
                    if str1[i-1] == str2[j-1]:
                        subCost = 0
                    else:
                        subCost = 1
                    matrix[i][j] = min(matrix[i-1][j]+1,matrix[i-1][j-1]+subCost,matrix[i][j-1] + 1)
                    if i > 1 and i < n+1 and j > 1 and j < m+1 and str1[i-1] == str2[j-2] and str1[i-2] == str2[j-1]:
                        matrix[i][j] = min(matrix[i][j],matrix[i-2][j-2]+1)
            return matrix[n][m]

#The last row with the current column's character
#The last column in this row where the characters matched
  def calculateDLDistance(self, str1, str2):
      n = len(str1) #col
      m = len(str2) #row

      uniqueSet = set(list(str1)+list(str2))
      alphabetLen = len(uniqueSet)
      da = {}#[0 for i in range(alphabetLen)]#new array of |Σ| integers

      d = [[0 for col in range(m+2)] for row in range(n+2)]#a 2-d array of integers, dimensions length(a)+2, length(b)+2
      #note that d has indices starting at −1, while a, b and da are one-indexed.

      maxdist = n+m
      d[0][0] = maxdist
      for i in range(1,n+2):
          d[i][0] = maxdist
          d[i][1] = i-1

      for j in range(1,m+2):
          d[0][j] = maxdist
          d[1][j] = j-1

      for i in range(2,n+2):
          db = 0 #Column of last match on this row
          for j in range(2,m+2):
              k = da.get(str2[j-2],0) #the current column's character
              l = db
              if str1[i-2] == str2[j-2]:
                  cost = 0
                  db = j
              else:
                  cost = 1
              d[i][j] = min(d[i-1][j-1] + cost,  #substitution
                    d[i][j-1] + 1,     #insertion
                    d[i-1][j] + 1,     #deletion
                    d[k-1][l-1] + (i-k-1) + 1 + (j-l-1)) #transposition
          da[str1[i-2]] = i
      return d[n+1][m+1]
