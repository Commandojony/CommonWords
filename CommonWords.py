
import sys



file_path = 'readme.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    file_content = ''.join(lines)

arr =file_content.split(" ")


count_words = lambda arr: {word: arr.count(word) for word in set(arr)}

dictionary = count_words(arr)

sort_words = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)


try:
    n = int(sys.argv[1])
    
    n_words  = lambda lst, n: sorted(lst, key=lambda x: x[1], reverse=True)[:n]

    print(n_words(sort_words,n))

except Exception as e:
        print(e)



