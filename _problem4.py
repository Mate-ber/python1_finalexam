
def count_dups(str_dups):
    dict_letters = {}
    ans = 0
    for i in range( len(str_dups) ):
        if str_dups[i] in dict_letters:
            if dict_letters[str_dups[i]] == 1:
                ans += 1
            dict_letters[str_dups[i]] += 1
        else:
            dict_letters[str_dups[i]] = 1
    return ans


str_dups = input("Write string here: ")

print(count_dups(str_dups.lower() ))