texts_info = {}
sorted_text_info = {}

#'first_couplet.txt', 'chorus_secondcouplet.txt', 'chorus_thirdcouplet.txt'
t1, t2, t3 = 'first_couplet.txt', 'chorus_secondcouplet.txt', 'chorus_thirdcouplet.txt'

def text_open(text):
    with open(text, 'r', encoding='utf8') as file:
        return file.readlines()

def count_lines(text):
    with open(text, 'r', encoding='utf8') as file:
        n = 0
        for string in file:
            n += 1
        texts_info[text] = n
    return n

def sort(a,b,c) -> None:
    number_of_lines = sorted([count_lines(a), count_lines(b), count_lines(c)])

    while len(number_of_lines) > 0:
        for name, lines in texts_info.items():
            if len(number_of_lines) >= 1:
                if lines == min(number_of_lines):
                    sorted_text_info[name] = lines
                    number_of_lines.remove(lines)
            else:
                sorted_text_info[name] = lines

            
    return sorted_text_info
                

sort(t1,t2,t3)

def join_texts():
    with open('merged_text', 'w', encoding='utf8') as merge:
        for name, count in sorted_text_info.items():
            merge.write(f'{name}\n{count}\n')
            merge.writelines(text_open(name))
    return print('Файлы объединены! в "merged_text.txt"')

join_texts()