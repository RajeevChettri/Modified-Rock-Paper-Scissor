from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    result = ""
    user_choice = ""
    computer_choice = ""

    if request.method == "POST":
        user_input = request.form.get("choice")
        options = {"r": "Rock", "p": "Paper", "s": "Scissor"}
        rules = {
            ("r", "s"): "🎉 You Win!",
            ("s", "p"): "🎉 You Win!",
            ("p", "r"): "🎉 You Win!",
            ("s", "r"): "😢 You Lose!",
            ("p", "s"): "😢 You Lose!",
            ("r", "p"): "😢 You Lose!"
        }

        if user_input in options:
            user_choice = options[user_input]
            computer_key = random.choice(["r", "p", "s"])
            computer_choice = options[computer_key]

            if user_input == computer_key:
                result = "🤝 It's a Draw!"
            else:
                result = rules.get((user_input, computer_key), "Something went wrong.   ")
        else:
            result = "Invalid input."

    return render_template("index.html", result=result, user=user_choice, computer=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)