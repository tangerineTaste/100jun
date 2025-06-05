# 입력 제일 마지막 줄에서 완성해야 하는 건물의 번호를 가르킨다
# 마지막 건물부터 시작하여 앞 건물 순서로 이동
# 2개 이상의 건물들이 동시에 건설되어 질 수 있다.
# 이전 건물 2개 이상인 경우 이전 건물들이 모두 건설되어야 시작할 수 있다.
# 마지막에서 부터 시작하여 먼저 길을 찾아낸 후 시작점을 리스트로 저장하여 진행
# 각 갈라진 길끼리 서로 시간을 비교하여 최장시간만 계산

buildings_num, rules_num = map(int, input().split(' '))
buildings_delay = [int(building) for building in input().split(' ')]
rules = []
for i in range(rules_num):
    x, y = map(int, input().split(' '))
    rules.append([x,y])
finish = int(input())

for i in range(finish):
    pass