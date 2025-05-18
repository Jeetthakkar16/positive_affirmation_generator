from flask import Flask, render_template, request,session
import random

app = Flask(__name__)
app.secret_key = "jeet@1606"

# Define these OUTSIDE the route
emotion_base = {
    "tired": ["tired", "exhausted", "no energy", "drained"],
    "anxious": ["anxious", "nervous", "worried", "overthinking"],
    "sad": ["sad", "heartbroken", "upset", "depressed", "down"],
    "angry": ["angry", "mad", "furious", "annoyed", "frustrated"],
    "demotivated": ["demotivated", "hopeless", "lost", "giving up"],
    "confident": ["confident", "strong", "capable", "empowered"],
    "happy": ["happy", "joyful", "excited", "grateful", "content"]
}

affirmations_data = {
    "tired": [
        "Your strength is greater than your struggle.",
        "It's okay to rest. You're still moving forward.",
        "You’ve come this far, and that’s powerful.",
        "Rest is productive too — you deserve it."
    ],
    "anxious": [
        "You are in control of your thoughts and emotions.",
        "Your breath is your anchor — inhale calm, exhale stress.",
        "You are safe, grounded, and in control.",
        "Peace begins with you — and you’re doing just fine."
    ],
    "sad": [
        "Your emotions are valid, and healing takes time.",
        "You are not alone — brighter days are coming.",
        "Tough times don’t last, but tough people do.",
        "You are deeply loved and supported."
    ],
    "angry": [
        "You are in control of your responses, not your emotions.",
        "Letting go brings peace — you're choosing calm.",
        "Anger is a sign something matters — and you're strong enough to handle it.",
        "You’re bigger than your anger — peace is power."
    ],
    "demotivated": [
        "Every effort counts — even the small ones.",
        "You are building something beautiful, step by step.",
        "It’s okay to pause — but never stop believing in yourself.",
        "You’ve overcome before — you will again."
    ],
    "confident": [
        "You radiate confidence and courage.",
        "You are capable of anything you set your mind to.",
        "Your belief in yourself is your superpower.",
        "Keep going — you're doing amazing!"
    ],
    "happy": [
        "Happiness flows naturally through you.",
        "You deserve every bit of joy you feel.",
        "Your light brightens those around you.",
        "Celebrate your happiness — you’ve earned it!"
    ],
    "unknown": [
        "You are doing your best, and that is enough.",
        "You are worthy of love, care, and happiness.",
        "Whatever you're feeling is valid — you're growing through it.",
        "The fact that you showed up today means you're already strong."
    ],
    "blank": [
        "Please take a moment to reflect — how do you feel?",
        "It’s okay to not have the words yet. Start with your breath.",
        "You matter, even when you don’t know what to say.",
        "When you're ready, I'm here to support you with kind words."
    ]
}


def detect_emotion(user_input):
    user_input = user_input.lower().strip()
    if not user_input:
        return "blank"
    for emotion, keywords in emotion_base.items():
        for word in keywords:
            if word in user_input:
                return emotion
    return "unknown"

@app.route("/main", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if 'submit' in request.form:
            userinput = request.form.get('message')
            session['userinput']=userinput
            emotion = detect_emotion(userinput)
            affirmation = random.choice(affirmations_data[emotion])
            #return render_template('main.html', userinput=userinput, affirmation=affirmation)
        elif 'anotheraffirmation' in request.form:
            userinput=session.get('userinput')
            emotion = detect_emotion(userinput)
            affirmation=random.choice(affirmations_data[emotion])
            print(userinput ,"and", affirmation)
        return render_template('main.html',userinput=userinput,affirmation=affirmation)
    else:
        return render_template('main.html')

app.run(port=1000, host='0.0.0.0')

