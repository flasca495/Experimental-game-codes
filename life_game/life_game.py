import random
from js import document, setTimeout

#　以下で定数を定義
DEAD, ALIVE = 0, 1
COLORS = ["white", "red"]
SIZE = 20
COLS = 400 // SIZE
ROWS = 400 // SIZE

# 以下で描画対象のCanvasとコンテキストを取得
canvas = document.getElementById("canvas")
context = canvas.getContext("2d")

# 以下でセル（2次元リスト）の初期配置をランダムに決定
cells = [[random.choice([DEAD, ALIVE]) for x in range(COLS)]
         for y in range(ROWS)]

# 以下で関数を定義
def next_generation(cells):
    """次の世代の処理を行う関数"""
    # 以下で次世代のセルの状態をすべて死で初期化
    new_cells = [[DEAD] * COLS for _ in range(ROWS)]

    # 以下で全セルをチェック
    for y in range(ROWS):
        for x in range(COLS):
            # ルールに従って次世代の状態を決定
            count = count_alive_cells(cells, x, y)
            if cells[y] [x] == ALIVE: # 生きているセル
                if count == 2 or count == 3:
                    new_cells[y][x] = ALIVE
            else: # 死んでいるセル
                if count == 3:
                    new_cells[y][x] =ALIVE
    return new_cells

def count_alive_cells(cells, x, y):
    """周囲(8方向)の生きているセルの数をカウント"""
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS:
                count += cells[ny][nx]
    return count

def draw_canvas():
    """セルの状態をCanvasに描画する関数"""
    for y in range(ROWS):
        for x in range(COLS):
            color = COLORS[cells[y][x]]
            context.fillStyle = color
            context.fillRect(x*SIZE, y*SIZE, SIZE, SIZE)
            context.strokeRect(x*SIZE, y*SIZE, SIZE, SIZE)

def update():
    """定期的に処理を行う関数"""
    global cells
    cells = next_generation(cells)
    draw_canvas()
    setTimeout(update, 500) # 500ミリ秒後に再度実行

update() # 最初の描画
