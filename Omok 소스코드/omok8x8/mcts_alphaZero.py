# -*- coding: utf-8 -*-
"""
알파고 제로 스타일의 몬테 카를로 트리 검색:
정책 가치 네트워크를 사용하여 나뭇잎 노드 검색 및 평가

@author: 오목조목 팀 in Hanseo University
"""

import numpy as np
import copy


def softmax(x):
    probs = np.exp(x - np.max(x))
    probs /= np.sum(probs)
    return probs


class TreeNode(object):
    """
     MCTS 트리의 노드
     각 노드는 노드의 값 Q, 그리고 이전 선택확률 P, 이전에 조정된 방문 점수 U를 추적
    """

    def __init__(self, parent, prior_p):
        self._parent = parent
        self._children = {}  # a map from action to TreeNode
        self._n_visits = 0
        self._Q = 0
        self._u = 0
        self._P = prior_p

    def expand(self, action_priors):
        """
            자식노드를 생성함으로 트리를 확장한다.
            action_priors : 정책 기능에 따른
            액션들과 그의 이전확률에 대한 튜플 리스트

        """
        for action, prob in action_priors:
            if action not in self._children:
                self._children[action] = TreeNode(self, prob)

    def select(self, c_puct):
        """액션값 Q와 보너스 u(P)를 더한 값을 가진 자식 노드 중
        가장 큰 값을 가진 자식노드 하나를 선택한다
        Return: A tuple of (action, next_node)
        """
        return max(self._children.items(),
                   key=lambda act_node: act_node[1].get_value(c_puct))

        """자식들 중, UCT, selection value가 가장 높은 노드를 반환"""


    def update(self, leaf_value):
        """leaf 평가로부터 노드의 값을 Update 한다.
           leaf_value : 현재 플레이어의 관점에서 하위 트리 의 평가 값
        """

        """방문횟수 count"""
        self._n_visits += 1

        """모든 방문에 대한 평균적인 값인 Q 업데이트"""
        self._Q += 1.0*(leaf_value - self._Q) / self._n_visits

    def update_recursive(self, leaf_value):
        """update()함수와 유사하나, 모든 부모노드에 대해 재귀적으로 적용된다.
           부모 노드가 아닌 경우, 먼저 이 노드의 상위노드 부터 업데이트되어야함
        """

        if self._parent:
            self._parent.update_recursive(-leaf_value)
        self.update(leaf_value)

    def get_value(self, c_puct):
        """Calculate and return the value for this node.
        It is a combination of leaf evaluations Q, and this node's prior
        adjusted for its visit count, u.
        c_puct: a number in (0, inf) controlling the relative impact of
            value Q, and prior probability P, on this node's score.

            해당 노드의 값을 계산하고 리턴해준다.
            leaf 평가치인 Q, 그리고 이 노드의 이전 조정된 방문횟수 U와의 조합이 값이 되며,
            c_puct : 0~무한대의 숫자로, 현재 노드의 점수에서 Q,P값에 상대적 영향
            을 제어하는 숫자이다 UCT-selection funtion를 활용.
        """
        self._u = (c_puct * self._P *
                   np.sqrt(self._parent._n_visits) / (1 + self._n_visits))

        """UCT-selection funtion"""
        return self._Q + self._u
        """Q의 값은 N번의 ACTION이 있었을때의 승리횟수//N번의 ACTION이 있었을 때의 시뮬횟수"""

    def is_leaf(self):
        """이 노드 아래에 확장된 노드가 없는지 확인하는 fn"""
        return self._children == {}

    def is_root(self):
        return self._parent is None


class MCTS(object):
    """몬테 카를로 트리 검색의 구현."""

    def __init__(self, policy_value_fn, c_puct=5, n_playout=10000):
        """
        policy_value_fn: board state 를 취하고, (액션, 확률) 튜플과 현재 플레이어의
        [-1,1] 사이의 점수(즉, 현재 플레이어의 관점에서 엔드 게임 점수의 예상 값)를
        리턴해주는 기능이다.
        c_puct: 탐사가 최대가치 정책에 얼마나 빨리 수렴되는지 제어하는 0~무한대의 숫자.
                값이 높을수록 이전 것에 더욱 의존한다.(데이터셋에 의존도)
        """
        self._root = TreeNode(None, 1.0)
        self._policy = policy_value_fn
        self._c_puct = c_puct
        self._n_playout = n_playout

    def _playout(self, state):
        """뿌리 노드부터 자식노드(leap)까지 한번의 플레이아웃을 실행하여, leap의 value를
        얻고 부모노드로 다시 프로퍼게이팅(값을 올려줌, 퍼뜨림)한다. 상태는 인플레이스에서
        수정됨으로, 반드시 스테이트를 카피(사본)하여 구한다.
        """
        node = self._root
        while(1):
            if node.is_leaf():
                """자식 노드가 비었으면, break"""
                break
            """다음 동작을 그리디(정책)하게 정한다."""
            action, node = node.select(self._c_puct)
            state.do_move(action)


        """  (액션, 확률) tuples p 목록과 
        또한 [-1, 1]사이의 점수 v를 출력하는 네트워크(policy_value_net)를 
        사용하여 현재 플레이어에 대한 리프을 평가한다"""
        action_probs, leaf_value = self._policy(state)
        #print(state.states, leaf_value)
        # Check for end of game.
        end, winner = state.game_end()
        if not end:
            node.expand(action_probs)
        else:
            """end state-즉 경기가 끝나는 보드상황시 'true' 리프 가치를 return한다."""
            if winner == -1:  # tie
                leaf_value = 0.0
            else:
                leaf_value = (
                    1.0 if winner == state.get_current_player() else -1.0
                )

        """이 단계에서의 방문횟수와 가치를 update한다."""
        node.update_recursive(-leaf_value)

    def get_move_probs(self, state, temp=1e-3):
        """모든 playouts을 순차적으로 실행하고, 사용가능한 동작과 해당 확률을 반환한다.
         state : 현재 게임의 상태 ( 24 : 1, 36 : 2  ...)
         temp : 0~1사이의 파라미터로, 탐사수준을 제어함
        """
        for n in range(self._n_playout):
            """내가 지정한 n_platout 숫자 만큼, 현재 상태를 카피하고, 
            카피한 현재상태를 매개변수로 하여 _playout 함수를 실행시킨다.
            """
            state_copy = copy.deepcopy(state)
            self._playout(state_copy)

        """루트노드의 방문횟수를 기준으로 이동확률을 계산한다."""

        act_visits = [(act, node._n_visits)
                      for act, node in self._root._children.items()]
        #for act, node in self._root._children.items():
        #    print(node._Q)

        acts, visits = zip(*act_visits)
        act_probs = softmax(1.0/temp * np.log(np.array(visits) + 1e-10))
        return acts, act_probs

    def update_with_move(self, last_move):
        """서브트리에 대해 이미 알고 있는 정보를 가지고, 그다음 트리로 향한다.
        """
        if last_move in self._root._children:
            self._root = self._root._children[last_move]
            self._root._parent = None
        else:
            self._root = TreeNode(None, 1.0)

    def __str__(self):
        return "MCTS"


class MCTSPlayer(object):
    """AI player based on MCTS"""

    def __init__(self, policy_value_function,
                 c_puct=5, n_playout=2000, is_selfplay=0):
        self.mcts = MCTS(policy_value_function, c_puct, n_playout)
        self._is_selfplay = is_selfplay

    def set_player_ind(self, p):
        self.player = p

    def reset_player(self):
        self.mcts.update_with_move(-1)

    def get_action(self, board, temp=1e-3, return_prob=0):
        sensible_moves = board.availables
        """현재 보드에서 착수가능한 좌표 반환"""
        #show_probsboard = [[0 for i in range(0,  8)] for j in range(0, 8)]

        """ 알파고 제로 논문에서 처럼 MCTS가 반환한 pi벡터"""
        move_probs = np.zeros(board.width*board.height)
        """선택확률리스트 8*8사이즈의 0으로 채워진 리스트로 초기화"""
        if len(sensible_moves) > 0:
            """착수할 수 있는 경우가 있다면,
               현재보드와 탐사 깊이를 매개변수로 삼아, 사용가능한 동작과 해당 확률을 
               반환한다.
            """
            acts, probs = self.mcts.get_move_probs(board, temp)
            move_probs[list(acts)] = probs
            print(move_probs)


        #    for i in range(0, 64):
        #        show_probsboard[i//8][i%8] = round(move_probs[i], 4)
        #    for x in range(0 , 8):
        #             print("[", show_probsboard[x][0], show_probsboard[x][1],show_probsboard[x][2],show_probsboard[x][3],
        #                 show_probsboard[x][4],show_probsboard[x][5],show_probsboard[x][6],show_probsboard[x][7],
        #                 "]")

        #    print("\n")  ~~ 현재 선택가능성 표시

            if self._is_selfplay:
                # add Dirichlet Noise for exploration (needed for
                # self-play training)
                move = np.random.choice(
                    acts,
                    p=0.75*probs + 0.25*np.random.dirichlet(0.3*np.ones(len(probs)))
                )
                # update the root node and reuse the search tree
                self.mcts.update_with_move(move)
            else:
                # with the default temp=1e-3, it is almost equivalent
                # to choosing the move with the highest prob
                move = np.random.choice(acts, p=probs)
                # reset the root node

                self.mcts.update_with_move(-1)
                location = board.move_to_location(move)
                print("AI move: %d,%d\n" % (location[0], location[1]))

            if return_prob:
                return move, move_probs
            else:
                return move
        else:
            print("WARNING: the board is full")

    def __str__(self):
        return "MCTS {}".format(self.player)
