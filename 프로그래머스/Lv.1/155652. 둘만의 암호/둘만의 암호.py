def solution(s, skip, index):
    result = ''
    for i in s:
        char_to_num = ord(i)
        number = 0
        while number < index:
            char_to_num += 1
            if char_to_num == 123:
                char_to_num = ord("a")  
            if chr(char_to_num) not in skip:
                number += 1
            
        result += chr(char_to_num)
    return result