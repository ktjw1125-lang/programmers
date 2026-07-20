def solution(num_list):
    mult = 1
    tot = 0
    
    for _ in range(len(num_list)):
        mult *= num_list[_]
    for _ in range(len(num_list)):
        tot += num_list[_]
    tot = tot **2
    
    return 1 if mult<tot else 0