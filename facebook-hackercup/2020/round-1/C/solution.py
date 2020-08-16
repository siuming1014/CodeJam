from collections import deque
import time
import math


def nC2(n):
    return int(n * (n - 1) / 2)


def solve(ii, N, K, S, Es, A, B, C):
  # calculate all E
  if K < N - 1:
    i = K + 2
    while i <= N:
      i_ = i - 1
      # E = ( (A % i_) * (Es[-2] % i_) + (B % i_) * (Es[-1] % i_) + C % i_ ) % i_ + 1
      E = (A * Es[-2] + B * Es[-1] + C) % i_ + 1
      Es.append(E)
      i += 1

  # print('len(Es)', len(Es))
  # print('N', N)

  # build adj list
  adj_lst = [[] for _ in range(N)]
  for i_, E in enumerate(Es):
    i = i_ + 1
    j = E - 1
    adj_lst[i].append(j)
    adj_lst[j].append(i)

  # print(adj_lst)

  # define function for tree traversal
  sym_idx = {"*": 0, "#": 1}

  def traverse(r, cur_sym, comp_idx, visited, pending, pending_set, components, comp_links):
    s = deque()
    s.append(r)
    # print('traverse', 's', s, 'components', components)
    while len(s):
      # time.sleep(0.2)
      node = s.pop()
      # print('node', node, 'S[node]', S[node], 'cur_sym', cur_sym)
      if S[node] == cur_sym:
        visited[node] = True
        components[sym_idx[cur_sym]][comp_idx].append(node)
        s.extend([_ for _ in adj_lst[node] if not visited[_] and _ not in pending_set])
      else:
        components[sym_idx[S[node]]].append([])
        comp_links[sym_idx[S[node]]].append([])

        new_comp_idx = len(components[sym_idx[S[node]]]) - 1
        pending.append((node, S[node], new_comp_idx))
        pending_set.add(node)

        comp_links[sym_idx[S[node]]][new_comp_idx].append(comp_idx)
        comp_links[sym_idx[cur_sym]][comp_idx].append(new_comp_idx)
      # print('s', s, 'components', components)
  
  # declare a list "visited"
  visited = [False] * N
  # declare a queue "pending" for storing pending node of another group
  pending = deque()
  pending.append((0, S[0], 0))  # node, sym, comp_idx
  pending_set = set([0])
  # declare a dict of list of list "components" and "comp_links"
  components = ([], [])  # * #
  components[sym_idx[S[0]]].append([])
  comp_links = ([], [])
  comp_links[sym_idx[S[0]]].append([])
  
  # traverse the tree to identify components
  while len(pending):
    # print('pending', pending)
    r, cur_sym, comp_idx = pending.popleft()
    pending_set.remove(r)
    traverse(r, cur_sym, comp_idx, visited, pending, pending_set, components, comp_links)
  
  comp_deg = tuple([len(c) for c in c_of_sym] for c_of_sym in components)
  # print('components', components)
  # print('comp_deg', comp_deg)
  # print('comp_links', comp_links)
  # print('len(components[0])', len(components[0]))
  # print('len(components[1])', len(components[1]))

  def f(n):
    return sum([int(r * (n - r)) for r in range(1, n)])

  if len(components[0]) == 0:
    return 0, int(f(N))
  elif len(components[0]) == 1:
    l0 = len(components[0][0])
    return nC2(l0), int(f(l0) + sum(f(len(c)) + int(len(c) * (N - len(c))) for c in components[1]))
  # elif len(components[0]) == 1 and len(components[1]) == 0:
  #   return nC2(N), int(f(N))
  # elif len(components[0]) == 1 and len(components[1]) == 1:
  #   l0 = len(components[0][0])
  #   l1 = len(components[1][0])
  #   return nC2(l0), int(f(l0) + f(l1) + l0 + l1)
  # elif len(components[0]) == 1 and len(components[1]) == 2:
  #   l0 = len(components[0][0])
  #   l10 = len(components[1][0])
  #   l11 = len(components[1][1])
  #   return nC2(l0), int(f(l0) + f(l10) + f(l11) + l10 * (l0 + l11) + l11 * (l0 + l10))

  comp_visited = [False] * len(components[0])

  s1 = deque()
  s1.append(0)
  max_sum = -1
  max_pairs = None
  while len(s1):
    n1 = s1.pop()
    parent_deg = len(components[0][n1])
    comp_visited[n1] = True

    for n2 in comp_links[0][n1]:
      for _n1 in comp_links[1][n2]:
        if not comp_visited[_n1]:
          s1.append(_n1)
          cur_sum = parent_deg + len(components[0][_n1])
          if cur_sum > max_sum:
            max_sum = parent_deg + len(components[0][_n1])
            max_pairs = {(n1, _n1) if n1 > _n1 else (_n1, n1)}
          if cur_sum == max_sum:
            max_pairs.add((n1, _n1) if n1 > _n1 else (_n1, n1))

  # print('max_pairs', max_pairs)
  return nC2(max_sum), sum(int(2 * len(components[0][pair[0]]) * len(components[0][pair[1]])) for pair in max_pairs)


def print_ans(print_fun, A):
  print_fun(' '.join(map(str, A)) + '\n')

if __name__ == '__main__':
  N_lst = []
  K_lst = []
  S_lst = []
  Es_lst = []
  A_lst = []
  B_lst = []
  C_lst = []

  T = int(input())
  for i in range(T):
    N, K = map(int, str(input()).split(' '))
    N_lst.append(N)
    K_lst.append(K)
    S_lst.append(str(input()))
    Es = list(map(int, str(input()).split(' ')))
    Es_lst.append(Es)
    A, B, C = map(int, str(input()).split(' '))
    A_lst.append(A)
    B_lst.append(B)
    C_lst.append(C)
      
          
  with open('output.txt', 'w') as fin:
    for i in range(T):
      fin.write(f'Case #{i + 1}: ')
      print_ans(fin.write, solve(i, N_lst[i], K_lst[i], S_lst[i], Es_lst[i], A_lst[i], B_lst[i], C_lst[i]))