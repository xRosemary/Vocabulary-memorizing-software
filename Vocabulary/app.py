from flask import Flask, render_template, request
from Vocabulary.interaction import Interaction
import random
import numpy as np

app = Flask(__name__)

interaction = Interaction()
wordlist, candidates = interaction.getlist()


@app.route('/')
def reIndex():
    return render_template('index.html')


@app.route('/learn')
def reLearn():
    return render_template('learn.html')


@app.route('/req/word', methods=["post"])
def getWord():
    word = wordlist.pop(1)
    item = {"ID": int(word[0]),
            "WORD": word[1],
            "PRONOUNCE": word[2],
            "PHONETIC": word[3],
            "PARAPHRASE": word[4],
            "Candidate": list(np.append(random.sample(candidates, 3), word[4]))
            }
    return item


if __name__ == '__main__':
    app.run()
