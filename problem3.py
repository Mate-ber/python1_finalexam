
def solution(_str):
    str_sz = len(_str)
    ans = ""
    if str_sz%2==0:
        ans += _str[str_sz//2-1]
    ans+=_str[str_sz//2]
    return ans


str_mid = input("Write string here: ")
print(solution(str_mid))