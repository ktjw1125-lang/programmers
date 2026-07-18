def solution(num_list):
    answer = 0
    e = ''
    o = ''
    for _ in range(len(num_list)):
        if num_list[_] %2 == 0:
            e += str(num_list[_])
        else:
            o += str(num_list[_])
    answer = int(o) +int(e)
    return answer