def solution(code):
    answer = ''
    mode = False
    for idx in range(len(code)):
        if code[idx] == str(1):
            mode = not mode
            continue
        if mode == 0:
            if idx %2 ==0: answer += code[idx]
        else: 
            if idx %2 !=0: answer += code[idx]
    
    return "EMPTY" if answer == "" else answer