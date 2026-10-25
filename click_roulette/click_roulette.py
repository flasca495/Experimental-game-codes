import random
from pyscript import document
from js import setTimeout

def start(event):
    disp = document.getElementById("disp")
    disp.innerText = ""
    roulette = document.getElementById("roulette")
    roulette.style.animation = "spin 2s linear infinite"
    setTimeout(stop, 2000)

def stop():
    r = random.randint(0, 36)
    if r == 0:
        color = "green"
    elif r % 2 ==0:
        color = "black"
    else:
        color = "red"
    disp = document.getElementById("disp")
    disp.innerText = str(r)
    disp.style.backgroundColor = color
    roulette = document.getElementById("roulette")
    roulette.style.animation = "none"
