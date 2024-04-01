from flask import Flask, render_template, request
from random import choice

app = Flask(__name__)

# Load images
rock_img = "rock.png"
paper_img = "paper.png"
scissors_img = "scissors.png"
comp_images = {
    "rock": "rockcomp.png",
    "paper": "papercomp.png",
    "scissors": "scissorscomp.png"
}

# Main route to serve the game interface
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle game actions
@app.route('/play', methods=['POST'])
def play():
    # Get the user's choice from the form
    user_choice = request.form['choice']

    # Generate computer's choice
    comp_choice = choice(["rock", "paper", "scissors"])

    # Determine the winner
    winner = ""
    if user_choice == comp_choice:
        winner = "It's a Tie!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        winner = "You Win!"
    else:
        winner = "Computer Wins!"

    return render_template('play.html', user_choice=user_choice, comp_choice=comp_choice, winner=winner,
                           user_img=user_choice + ".png", comp_img=comp_images[comp_choice])

if __name__ == '__main__':
    app.run(debug=True)
