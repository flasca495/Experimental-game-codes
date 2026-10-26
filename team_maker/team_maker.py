
import random
from pyscript import document


def make_teams(event):
    names_text = document.getElementById("names").value
    count_text = document.getElementById("team_count").value

    names = [
        name.strip()
        for name in names_text.splitlines()
        if name.strip()
    ]

    message = document.getElementById("message")
    result = document.getElementById("result")

    message.innerText = ""
    result.innerHTML = ""

    if not names:
        message.innerText = "名前を入力してください。"
        return

    team_count = int(count_text)

    if len(names) < team_count:
        message.innerText = "参加者の人数がチーム数より少ないです。"
        return

    names = random.sample(names, len(names))

    teams = [[] for _ in range(team_count)]

    for i, name in enumerate(names):
        teams[i % team_count].append(name)

    for i, team in enumerate(teams):
        box = document.createElement("div")
        box.className = "team"

        heading = document.createElement("h2")
        heading.innerText = f"チーム {i + 1}"
        box.appendChild(heading)

        for name in team:
            member = document.createElement("p")
            member.innerText = name
            box.appendChild(member)

        result.appendChild(box)
