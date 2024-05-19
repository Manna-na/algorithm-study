def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    
    def is_valid(word):
        for sound in valid_sounds:
            if sound * 2 in word:
                return False
        for sound in valid_sounds:
            word = word.replace(sound, ' ')
        return word.strip() == ''
    
    count = 0
    for word in babbling:
        if is_valid(word):
            count += 1
    
    return count