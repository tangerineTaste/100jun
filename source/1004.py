# 도착점 혹은 출발점이 원안에 있다면 무조건 한번은 지나친다
# 단, 도착점과 출발점이 동시에 한 원안에 있는 경우는 지나치지 않는다

term = int(input())
count = []
for t in range(term):
    c = 0
    gps = [int(i) for i in input().split(' ')]
    circles_count = int(input())
    circles = []
    for i in range(circles_count):
        circles.append([int(i) for i in input().split(' ')])
    for circle in circles:
        if ((gps[0]-circle[0])**2 + (gps[1]-circle[1])**2)**0.5 < circle[2] and \
            ((gps[2]-circle[0])**2 + (gps[3]-circle[1])**2)**0.5 < circle[2]:
            pass
        elif((gps[0]-circle[0])**2 + (gps[1]-circle[1])**2)**0.5 < circle[2] or \
            ((gps[2]-circle[0])**2 + (gps[3]-circle[1])**2)**0.5 < circle[2]:
            c += 1
    count.append(c)
for t in range(term): 
    print(count[t])