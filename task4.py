#!/usr/bin/python
import editdistance

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word: str) -> None:

        self.dic[word] = True
        subStr = ""
        for i in range(len(word)-1):
            subStr += word[i]
            if subStr not in self.dic:
                self.dic[subStr] = False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.dic:
            if self.dic[word]:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.dic

#def dfs(

def task4(dictionary, raw):
    minLst = []
    with open(raw,"r") as f:
        rawData = f.read()
    rawLst = rawData.split("\n")
    with open(dictionary,"r") as f:
        dicData = f.read()
    dicLst = set(dicData.split("\n"))
    obj = Trie()
    ed = editdistance.EditDistance()
    for word in dicLst:
        obj.insert(word)
    #compare all the words in the dictionary until you find the minimum distance of the current word in raw.txt. 
    #test = {}
    for mispelledWord in rawLst:
        if obj.search(mispelledWord):
            minLst.append(0)
        else:
            #subStr = ""
            theMin = len(mispelledWord)
            for word in dicLst:
                curMin = ed.calculateOSADistance(mispelledWord,word)
  #          for ch in word:
 #               subStr += ch
                #if obj.startsWith(subStr):
                 #   curMin = ed.calculateOSADistance(subStr,word)
                if curMin < theMin:
                    theMin = curMin
                    #test[theMin] = subStr
                    #prevMin = curMin
            minLst.append(theMin)
    # return list has the same length with raw.txt
    #print(len(minLst)==len(rawLst))
    return minLst#return : a list of min_distance of each word in the raw.txt


#print(task4("dictionary.txt", "raw.txt"))
