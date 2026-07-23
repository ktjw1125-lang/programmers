def solution(numLog):
    answer = ''
    count = 0
    for _ in numLog:
        if count == 0:
            count += 1
            previous = int(_)
            continue
            
        if int(_) - previous == 1:
            answer += 'w'
        elif int(_) - previous == -1:
            answer += 's'
        elif int(_) - previous == 10:
            answer += 'd'
        elif int(_) - previous == -10:
            answer += 'a'

        previous = int(_)
        count += 1
    return answer