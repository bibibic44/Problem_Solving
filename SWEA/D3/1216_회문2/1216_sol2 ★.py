# 속도 개선
# 중심을 잡고 양 옆으로 이동해가며 펠린드롬 비교
# 한 줄짜리 string은 프로그래머스 코드 참고
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_case = input()
    a = [input() for _ in range(100)]
    # reverse_a는 세로를 검사하기 위해 a의 col과 row를 반전
    reverse_a = list(map(list, zip(*a)))

    ans = 1
    for x in range(100):
        for i in range(100):
            # 가로
            # 길이가 홀수인 좌우 대칭(팰린드롬) 확인
            tmp_odd = 1
            for j in range(1, i+1):
                if 0 <= i - j and i + j < 100 and a[x][i - j] == a[x][i + j]:
                    tmp_odd += 2
                # 좌우 대칭이 아니면 바로 break 한다.
                else:
                    break
            # 길이가 짝수인 좌우 대칭 확인
            tmp_even = 0
            for j in range(0, i+1):
                if 0 <= i - j and i + j + 1 < 100 and a[x][i - j] == a[x][i + j + 1]:
                    tmp_even += 2
                else:
                    break

            # ans와 가로 tmp 비교
            ans = max(ans, tmp_odd, tmp_even)

            # 세로
            # 길이가 홀수인 좌우 대칭(팰린드롬) 확인
            tmp_odd = 1
            for j in range(1, i+1):
                if 0 <= i - j and i + j < 100 and reverse_a[x][i - j] == reverse_a[x][i + j]:
                    tmp_odd += 2
                # 좌우 대칭이 아니면 바로 break 한다.
                else:
                    break
            # 길이가 짝수인 좌우 대칭 확인
            tmp_even = 0
            for j in range(0, i+1):
                if 0 <= i - j and i + j + 1 < 100 and reverse_a[x][i - j] == reverse_a[x][i + j + 1]:
                    tmp_even += 2
                else:
                    break

            # ans와 세로 tmp 비교
            ans = max(ans, tmp_odd, tmp_even)

    print('#{} {}'.format(tc, ans))
