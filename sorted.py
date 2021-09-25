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
            dict_files[counter] = file  


    sort = open('sorted.txt', 'a', encoding = 'utf8')
    for item in sorted(dict_files.keys()):
        temp_str = dict_files[item] + '\n' + str(item) +'\n'
        sort.write(temp_str)
            
        with open(dict_files[item], 'r', encoding = 'utf8')as text:
            all_text = text.readlines()
        text.close()
        for line in all_text:
            sort.write(line)
        sort.write('\n')

    sort.close()


make_sorted_txt()

        
