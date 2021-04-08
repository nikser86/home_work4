import list1


l = ('сс', 'строка2', '1строка1')
r = list1.match_ends(l)
print('strings where the string length is 2 or more and the first and last chars of the string are the same:', r, '\n')

wor = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
sort_words = list1.front_x(wor)
#print(sort_words)

l_t = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# sorted(student_tuples, key=itemgetter(2))
l_t1 = list1.sort_last(l_t)
#print(l_t1)

#s = list1.test(5, 5)

list1.main()