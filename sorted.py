import os
def make_sorted_txt():
    list_of_files = os.listdir()
    dict_files = {}
    for file in list_of_files:
        if file.endswith('.txt') and file != 'sorted.txt':
            with open(file, encoding = 'utf8') as f:
                counter = 0
                for line in f:
                    counter += 1
            dict_files[file] = counter  
    



    sort = open('sorted.txt', 'a', encoding = 'utf8')
    for item in dict(sorted(dict_files.items(), key=lambda item: item[1])):
        temp_str = item + '\n' + str(dict_files[item]) +'\n'
        sort.write(temp_str)
            
        with open(item, 'r', encoding = 'utf8') as text:
           for line in text:
               sort.write(line)
        sort.write('\n')

    sort.close()


make_sorted_txt()

        
