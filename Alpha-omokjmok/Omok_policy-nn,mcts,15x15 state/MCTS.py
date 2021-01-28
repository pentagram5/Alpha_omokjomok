#아래의 코드에서 많은 도움을 받았습니다.
# - 모두의 연구소: 이영무님 TicTacToe with MCTS : http://www.modulabs.co.kr/RL_library/7984
# - MCTS python Implementation : http://mcts.ai/code/python.html

from Omok import *
import copy
from math import *
import random
import rule
class Node:
    def __init__(self, state, prior_p , action=None, parent=None):
        self.state = state
        self.action = action
        self.parent_node = parent
        self.child_nodes = []
        self.n_wins = 0
        self.n_visits = 0
        self.untried_actions = state.get_possible_actions()
        self._P=prior_p
        self._Q = 0
        self._U = 0
        self.player = state.player

    def select_child_with_UCT(self):

        k = lambda c: c.n_wins/c.n_visits + sqrt(2 * self.n_visits / c.n_visits)
        print(self.n_visits, k)
        childs = sorted(self.child_nodes, key = k) # UCT 수식
        return childs[-1]

    def add_child(self, state, action, action_priors):
        n = Node(action = action, parent = self, state = copy.deepcopy(state), prior_p=action_priors)
        self.untried_actions.remove(action)
        self.child_nodes.append(n)
        return n

    def update(self, result):
        self.n_wins += result
        self.n_visits += 1

    def select(self, c_puct):
        """Select action among children that gives maximum action value Q
        plus bonus u(P).
        Return: A tuple of (action, next_node)
        """
        return max(self._children.items(),
                   key=lambda act_node: act_node[1].get_value(c_puct))


    def __repr__(self):
        return 'Action : %s W/V : %s \n'%(self.action, round(self.n_wins/self.n_visits, 3))


def MCTS_UCT(root_state, policy_value_fn, c_puct, n_simulation, default_policy=random.choice):
    # 현재는 tree_policy와 default_policy는 random.choice로 세팅
    # 추후에 critic과 actor로 대체
    print(root_state)
    root_node = Node(state=root_state, prior_p=1.0)
    _policy = policy_value_fn

    for i in range(n_simulation):
        if (i+1)%100 == 0:
            print('%s-th simulation on process'%(i+1), end='\r')
        node = root_node
        state = copy.deepcopy(root_state)

        #selection
        # root node에서 시작해서 현재까지 펼쳐진 child node 중 하나로 내려간다
        while node.untried_actions == [] and node.child_nodes != []:
            node = node.select_child_with_UCT()
            node.action, node = node.select(c_puct)
            win = state.do_action(node.action)
            action_pobs, leaf_value = _policy(node.state)
            if win == 1:
                leaf_value = -1.0
            elif win == 2:
                leaf_value = 1.0
            else:
                leaf_value = 0.0
                node.add_child(node.state, node.action, action_pobs)

        #Expansion
        # 아직 선택해보지 않은 action이 남았다면 (not-fully expanded), 해당 action을 선택하고 새로운 child node를 생성함
        if node.untried_actions != []:
            random_a = random.choice(node.untried_actions)
            state.do_action(random_a)

            node = node.add_child(state, random_a) # add child and descent tree

        #simulation
        # 선택된(selected) 혹은 확장된(expanded) node에서부터 게임이 끝날때까지 play
        while state.get_possible_actions() != []:
            random_a = default_policy(state.get_possible_actions())
            state.do_action(random_a)


        #BackPropagation
        while node != None:
            node.update(state.get_result(node.player))
            node = node.parent_node

    childs = sorted(root_node.child_nodes, key = lambda c: c.n_wins/c.n_visits)
    print('\n %s'%childs[-5:])

    best_child = sorted(childs, key = lambda c: c.n_visits)[-1]
    return best_child, best_child.action
