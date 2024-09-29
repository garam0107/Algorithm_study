import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())    # 일수, 인출횟수
use = list(int(input()) for _ in range(n))  # 일별 사용 금액
start = max(use)
end = sum(use)

# 이분탐색
while start <= end:
    mid = (start+end) // 2  # 인출할 금액
    charge = mid    # 인출한 금액
    cnt = 1         # 인출 횟수
    for i in range(n):
        if charge < use[i]:  # 가진 돈 부족하면 인출
            charge = mid
            cnt += 1
        charge -= use[i]     # 사용한거 차감
    # 인출횟수 초과하거나 인출 금액 부족할때
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
print(mid)