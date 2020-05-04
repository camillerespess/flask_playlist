from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

song_list = convert_to_dict('caring_songs.csv')

pairs_list = []
for s in song_list:
    pairs_list.append( (s['Song-Number'], s['Song']) )

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list)

@app.route('/song/<num>')
def song(num):
    music = song_list[int(num)- 1 ]
    return render_template('song.html', music=music)

if __name__ == '__main__':
    app.run(debug=True)
