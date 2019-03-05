
# coding: utf-8

# In[16]:


file = open('numbers.txt', 'r')
lst = []
for string in file:
    if int(string) not in lst:
        lst.append(int(string))
        lst.sort()
        minN = min(lst)
        maxN = max(lst)

    print("Message " + str(minN) + "-" + str(maxN) + " ", end="")

    if maxN - minN == len(lst) - 1:
        print("received RIGHT", end="")
    else:
        print("received WRONG: ", end="")
        n = 0
        package = True
        for i in range(minN + 1, maxN):
            for j in range(n, len(lst)):
                if i == lst[j]:
                    break
                if i < lst[j]:
                    if not package:
                        print(", ", end="")
                    print(i, end="")
                    package = False
                    n = j
                    break
        print(" missing")
    print("")

