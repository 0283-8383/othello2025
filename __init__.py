# Generation ID: Hutch_1764573066298_p4xlv2i9c (前半)

def myai(board, color):
    """
    オセロの最適な置き手を返す関数

    Args:
        board: 2次元配列(6x6または8x8)
        color: 置く色(1=BLACK, 2=WHITE)

    Returns:
        (column, row): 最も多くの石が取れる位置
    """

    BLACK = 1
    WHITE = 2
    opponent_color = WHITE if color == BLACK else BLACK

    rows = len(board)
    cols = len(board[0])

    # 8方向(上下左右と斜め)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def count_flips(row, col, direction):
        """指定方向でひっくり返せる石の数"""
        if board[row][col] != 0:
            return 0

        dr, dc = direction
        flips = 0
        r, c = row + dr, col + dc

        while 0 <= r < rows and 0 <= c < cols:
            if board[r][c] == 0:
                return 0
            if board[r][c] == color:
                return flips
            flips += 1
            r += dr
            c += dc

        return 0

    def get_total_flips(row, col):
        """指定位置で取れる石の総数"""
        total = 0
        for direction in directions:
            total += count_flips(row, col, direction)
        return total

    best_position = None
    max_flips = -1

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                flips = get_total_flips(row, col)
                if flips > 0 and flips > max_flips:
                    max_flips = flips
                    best_position = (col, row)

    return best_position if best_position else (0, 0)

# Generation ID: Hutch_1764573066298_p4xlv2i9c (後半)
