from flask import Flask, jsonify

app = Flask(__name__)

class Crop:
    def __init__(self, name, grow_time):
        self.name = name
        self.grow_time = grow_time
        self.time_planted = None
        self.is_grown = False

    def plant(self):
        self.time_planted = time.time()

    def water(self):
        if not self.time_planted:
            return "You need to plant a crop first!"
        if self.is_grown:
            return f"The {self.name} is already grown!"
        if time.time() - self.time_planted >= self.grow_time:
            self.is_grown = True
            return f"The {self.name} is now fully grown!"
        return f"The {self.name} needs more time to grow."

    def harvest(self):
        if not self.is_grown:
            return f"The {self.name} is not ready for harvest yet."
        self.is_grown = False
        self.time_planted = None
        return f"You harvested the {self.name}!"

crop = Crop("Wheat", 5)

@app.route('/plant', methods=['POST'])
def plant():
    crop.plant()
    return jsonify(message=f"Planted {crop.name}.")

@app.route('/water', methods=['POST'])
def water():
    message = crop.water()
    return jsonify(message=message)

@app.route('/harvest', methods=['POST'])
def harvest():
    message = crop.harvest()
    return jsonify(message=message)

if __name__ == '__main__':
    app.run(debug=True)
