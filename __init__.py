import math
from sakura import othello

BLACK = 1
WHITE = 2

# -------------------------
# 評価関数：位置の重み + 石数
# -------------------------
WEIGHTS = [
    [100, -20, 10, 10, -20, 100],
    [-20, -50, -2, -2, -50, -20],
    [10,  -2,  0,  0,  -2,  10],
    [10,  -2,  0,  0,  -2,  10],
    [-20, -50, -2, -2, -50, -20],
    [100, -20, 10, 10, -20, 100]
]

def evaluate(board, player):
    opp = BLACK if player == WHITE else WHITE
    score = 0

    for y in range(6):
        for x in range(6):
            if board[y][x] == player:
                score += WEIGHTS[y][x]
            elif board[y][x] == opp:
                score -= WEIGHTS[y][x]

    return score

# -------------------------
# Minimax + αβ
# -------------------------
def minimax(board, depth, player, maximizing, alpha, beta):
    moves = othello.legal_moves(board, player)
    opp = BLACK if player == WHITE else WHITE

    if depth == 0 or not moves:
        return evaluate(board, player), None

    best_move = None

    if maximizing:
        max_eval = -math.inf
        for move in moves:
            new_board = othello.copy_board(board)
            othello.put_and_reverse(new_board, player, move)

            eval, _ = minimax(new_board, depth - 1, opp, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = math.inf
        for move in moves:
            new_board = othello.copy_board(board)
            othello.put_and_reverse(new_board, player, move)

            eval, _ = minimax(new_board, depth - 1, opp, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval, best_move

# -------------------------
# AI のプレイヤー
# -------------------------
def myai(board, player):
    # AIのターンの処理をここで行います
    _, move = minimax(board, depth=4, player=player, maximizing=True, alpha=-math.inf, beta=math.inf)
    return move

# -------------------------
# 対戦用ラッパー
# -------------------------
def play_vs_strong_ai():
    board = othello.init_board()
    current = BLACK

    while True:
        print("\n=== Current Board ===")
        othello.print_board(board)

        moves = othello.legal_moves(board, current)
        if not moves:
            print("No moves. Turn skipped.")
            current = WHITE if current == BLACK else BLACK
            continue

        if current == BLACK:
            # 人間のターン
            print("Your turn (BLACK)")
            print("Legal moves:", moves)
            x, y = map(int, input("x y ? ").split())
            if (x, y) not in moves:
                print("Illegal move.")
                continue
            othello.put_and_reverse(board, current, (x, y))

        else:
            # AI のターン
            print("AI thinking…")
            move = myai(board, WHITE)
            print("AI move:", move)
            othello.put_and_reverse(board, WHITE, move)

        current = WHITE if current == BLACK else BLACK

# この関数を使ってAIと対戦できるように変更しました。
# AIのロジックを `myai` にまとめて、`othello.play(myai)` で呼び出せるようにしています。

# ここで対戦を開始する
#if __name__ == "__main__":
 #   othello.play(myai)
