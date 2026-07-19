def solution(schedules, timelogs, startday):
    answer = 0
    attendance = [True] * len(timelogs)
    schedules_max = []
    h = 0
    m = 0
    ms = ""
    temp = 0
    
    # schedules에 10분을 더한다
    for _ in range(len(schedules)):
        temp = schedules[_] +10
        h = temp //100
        m = temp %100
        if  m >= 60 : # 분이 60을 넘을경우 처리
            h += 1
            m = m %60
        if m == 0 : ms = "00"
        elif m <10 : ms = "0" + str(m)
        else: ms = str(m)
        if h == 24 : h = 0 # '시'가 24를 넘을경우 처리
        schedules_max.append( int( str(h) + ms ) )
    
    # 지각여부 확인
    for _ in range(len(timelogs)):
        for d in range(7):
            if (d + startday) %7 == 6 or (d + startday) %7 == 0: continue
            else:
                if timelogs[_][d] > schedules_max[_]:
                    attendance[_] = False
                    
    answer = attendance.count(True)
    return answer