
import random
from pyscript import document, when

# ボタンがクリックされたときに呼び出される関数
@when("click", "dice_button")
def show_dice_button(event):
    # 1から6までの整数をランダムに取得
    r = random.randint(1, 6)

    # idがdispのHTML要素を取得
    disp = document.getElementById("disp")

    # 表示するテキストを更新
    disp.innerText = str(r)
