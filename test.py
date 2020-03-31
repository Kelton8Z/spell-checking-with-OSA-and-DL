def calculateDLDistance(str1, str2):
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

      for i in range(2,n+1):
          db = 0 #Column of last match on this row
          for j in range(2,m+1):
              k = da.get(str2[j-1],0) #the current column's character
              l = db
              if str1[i-1] == str2[j-1]:
                  cost = 0
                  db = j
              else:
                  cost = 1
              d[i][j] = min(d[i-1][j-1] + cost,  #substitution
                    d[i][j-1] + 1,     #insertion
                    d[i-1][j] + 1,     #deletion
                    d[k-1][l-1] + (i-k-1) + 1 + (j-l-1)) #transposition
          da[str1[i-1]] = i
      return d[n][m]


str1 = "ca"
str2 = "abc"
print(calculateDLDistance(str1, str2))

str1 = "student"
str2 = "sutdeny"
print(calculateDLDistance(str1, str2))

