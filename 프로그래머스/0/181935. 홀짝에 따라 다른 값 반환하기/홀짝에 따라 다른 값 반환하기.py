def solution(n):
    answer = 0
    if n %2 != 0 :
        for _ in range(n):
            if (_+1) %2 != 0 : answer += _+1
    else:
        for _ in range(n):
            if (_+1) %2 == 0 : answer += (_+1) **2
    return answer