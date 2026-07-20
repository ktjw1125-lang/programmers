def solution(a, d, included):
    answer = 0
    for _ in range(len(included)):
        if included[_] == True: answer += a + (_)*d
    return answer