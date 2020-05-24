import pandas as pd
import numpy as ny
from jiwer import wer
import string
s1 = "I have, myself, full confidence that if all do their duty, if nothing is neglected, and if the best"
s2 = "I have myself full confidence that you be out with their duties nothing is knickknacks and if the best"
s3 = "It is this fate, I solemnly assure you, that I dread for you, when the time comes that you make your reckoning"
s4 = "this is fate I solemnly assure you that address for you when the time comes that you make a reckoning"
s5 = "Can we forge against these enemies a grand and global alliance, North and South, East and West"
s6 = "Kyrie Force against these enemies of grand and Global Alliance north and south east and west"
s7 = "Believe me, I who am speaking to you with full knowledge of the facts, and who tell you that nothing is lost for France."
s8 = "believe me I who am speaking to you with full knowledge of the facts and who tell you that nothing is false for France"
s9 = "I believe that in the history of the world, there has not been a more genuinely democratic struggle for freedom than ours"
s10 = "I believe that in the history of the world there has not been the more generally Democratic struggle for freedom than ours"
s11 = "U.S. confirms its 8th case of coronavirus; Pentagon to provide quarantine housing"
s12 = "us confirms is 8 case of Corona virus Pentagon to provide quarantine housing"
s13 = "一群初期外界普遍都在讨论病毒的来源其中最广泛传播的信息不乏指控武汉人是蝙蝠等也为病这种病毒感染人类"
s14 = "疫情初期，外界曾遍都在探讨病毒的来源，其中最广泛传播的讯息不乏指控武汉人吃蝙蝠等野味，令这种病毒感染人类."
s15 = "How sis months underwater sent this town on a search for its soul"
s16 = "How six months underwater sent this town I will search for is soap"
s17 = "The no-annual-fee cards that best the Chase Sapphire Reserve"
s18 = "the Noah annual see cars that best Chase Sapphire Reserve"
s19 = "Advanced indexing returns a copy of data rather than a view of it"
s20 = "Advanced indexing returns a copy of data rather than the office"
# s1 = "U.S. confirms its 8th case of coronavirus; Pentagon to provide quarantine housing "  #oringinal word in columns
# s2 = "us confirms is 8 case of Corona virus Pentagon to provide quarantine housing "
punctuation = list(string.punctuation)
def punc(string):
    s1 = ''
    for item in string:
        if item not in punctuation:
            s1 += item
    s1 = s1.upper()
    return s1
def word_list(string):
    lst = []
    data = string.split()
    for item in data:
        lst.append(item)
    return lst
# print(df)
def chr_in_list(string):
    lst = []
    for char in string:
        lst.append(char)
    return lst
def edit_distance(x1, x2):   #   reference:
    df = ny.zeros((len(x1)+1,len(x2) +1)).astype(dtype=ny.int32)  # initalizing the matrix of size len(x1),len(x2)
    df[0,1:] = ny.arange(1, len(x2)+1)
    df[1:,0] = ny.arange(1,len(x1)+1)   # 3 rows

    for j in range(1, len(x2) + 1):       # i = 1,2,3  rows
        for i in range(1, len(x1) + 1):   # j = 1,2  columns
            if x1[i - 1] == x2[j - 1]:
                # print("success")
                df[i, j] = df[i - 1, j - 1]  # if two words are equal, the number pass on to the next diagonal cube
            elif x1[i - 1] != x2[j - 1]:
                df[i, j] = min(df[i - 1, j] + 1, df[i, j - 1] + 1, df[i-1, j-1] + 1
                        )     #deletion #insertion and #substitution
    return df
def product0s(df,x1,x2):
    lstxx = []
    lstcolumns = ['']
    lstindex =['']
    lst = (len(x1) + 2) * [0]
    for i in range(len(x2)+2):
        lstxx.append(lst)
    for i in range(len(x2)):
        lstcolumns.append(x2[i])
    for j in range(len(x1)):
        lstindex.append(x1[j])
    df2 = pd.DataFrame(ny.array(df),
                       columns=lstcolumns, index=lstindex)
    return df2
def wer(x1,x2):
    lst1 = word_list(punc(x1))
    lst2 = word_list(punc(x2))
    x = edit_distance(lst1, lst2)
    # print(x)
    k = product0s(x, lst1, lst2)
    result = x[x.shape[0]-1,x.shape[1]-1]
    print(k)
    print(len(lst1)," of words in oringianl text ")
    print("The number or error is %d and the word error rate is %.2f percent" %(result, result/len(lst1)*100))
    return result
def charer(x1,x2):
    lst1 = chr_in_list(punc(x1))
    lst2 = chr_in_list(punc(x2))
    x = edit_distance(lst1, lst2)
    # print(x)
    k = product0s(x, lst1, lst2)
    result = x[x.shape[0]-1,x.shape[1]-1]
    print(k)
    print(len(lst1)," of characters in oringianl text")
    print("The number of error is %d and the characters error rate is %.2f percent" %(result, result/len(lst1)*100))
    return result
def sentence_e_r(x1,x2):
    if wer(x1,x2) == 0:
        print("no sentence error")
        return True
    else:
        return False
def main():
    print("#1")
    charer(s1,s2)
    wer(s1,s2)
    sentence_e_r(s1,s2)
    print("#2")
    charer(s3,s4)
    wer(s3,s4)
    sentence_e_r(s3,s4)
    print("#3")
    charer(s5,s6)
    wer(s5,s6)
    sentence_e_r(s5,s6)
    print("#4")
    charer(s7,s8)
    wer(s7,s8)
    sentence_e_r(s7,s8)
    print("#5")
    charer(s9,s10)
    wer(s9,s10)
    sentence_e_r(s9,s10)
    print("#6")
    charer(s11,s12)
    wer(s11,s12)
    sentence_e_r(s11,s12)
    print("#7")
    charer(s13,s14)
    wer(s13,s14)
    sentence_e_r(s13,s14)
    print("#8")
    charer(s15,s16)
    wer(s15,s16)
    sentence_e_r(s15,s16)
    print("#9")
    charer(s17,s18)
    wer(s17,s18)
    sentence_e_r(s17,s18)
    print("#10")
    charer(s19,s20)
    wer(s19,s20)
    sentence_e_r(s19,s20)
if __name__ == '__main__':
    main()



# for i in range(len(lst1)):
#     for j in range(len(lst2)):
#         if lst1[i] == lst2[j]:
#             print(lst1[i],lst2[j], "are the same" )
#         else:
#             print(lst1[i],lst2[j], "are different" )
# print(df.columns)
# print(df.index)
# df2 = pd.DataFrame(ny.array([[0, 0, 0, 0,0], [0, 0, 0, 0,0],[0, 0, 0, 0,0], [0, 0, 1, 1,0]]),
#                     columns=['','',lst1[0], lst1[1],lst1[2]], index = ['','',lst2[0],lst2[1]])
# def table(sentence1, sentence2):