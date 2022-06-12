# https://www.acmicpc.net/problem/2529
import sys

n = int(sys.stdin.readline().strip())
bracket = sys.stdin.readline().strip().split()


def compare(brac, num1, num2):
    """
    s[-1](=num1) 과 i(=num2) 가 bracket을 만족하는 숫자의 조합인지 확인한다.
    :param brac: 부등호
    :param num1: s의 마지막 성분
    :param num2: 탐색중인 i
    :return: 부등식의 만족 여부
    """
    if brac == ">":
        if num1 > num2:
            return True

    else:
        if num1 < num2:
            return True

def dfs_max(s, idx):
    """
    조건을 만족하는 최대값의 수를 찾아낸다
    :param s: stack
    :param idx: bracket[idx]에 대입할 index
    :return: 최대값의 수
    """
    # 길이가 n + 1이 되면 출력하고, 출력했다는 신호를 flag로서 보낸다.
    if len(s) == n + 1:
        print("".join(map(str, s)))
        return True

    for i in range(9, -1, -1):
        if len(s) == 0:
            s.append(i)
            flag = dfs_max(s, idx)
            # 만약 어느 한 가지의 끝에서 print가 실행되었을 경우, 바로 탐색을 전부 종료한다.
            if flag:
                return True
            s.pop()
        else:
            if i not in s and compare(bracket[idx], s[-1], i):
                s.append(i)
                flag = dfs_max(s, idx + 1)
                # 만약 어느 한 가지의 끝에서 print가 실행되었을 경우, 바로 탐색을 전부 종료한다.
                if flag:
                    return True
                s.pop()

def dfs_min(s, idx):
    """
    조건을 만족하는 최소값의 수를 찾아낸다
    :param s: stack
    :param idx: bracket[idx]에 대입할 index
    :return: 최소값의 수
    """
    # 길이가 n + 1이 되면 출력하고, 출력했다는 신호를 flag로서 보낸다.
    if len(s) == n + 1:
        print("".join(map(str, s)))
        return True

    for i in range(10):
        if len(s) == 0:
            s.append(i)
            flag = dfs_min(s, idx)
            # 만약 어느 한 가지의 끝에서 print가 실행되었을 경우, 바로 탐색을 전부 종료한다.
            if flag:
                return True
            s.pop()
        else:
            if i not in s and compare(bracket[idx], s[-1], i):
                s.append(i)
                flag = dfs_min(s, idx + 1)
                # 만약 어느 한 가지의 끝에서 print가 실행되었을 경우, 바로 탐색을 전부 종료한다.
                if flag:
                    return True
                s.pop()

dfs_max(s=[], idx=0)
dfs_min(s=[], idx=0)


