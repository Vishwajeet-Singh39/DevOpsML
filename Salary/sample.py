from flask import Flask, jsonify, render_template,request
import pickle
app = Flask(__name__,template_folder='template')


@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})

@app.route("/",methods=["GET"])
def home_page():
    return render_template('home_page.html')

@app.route('/salary')
def salary():
    return render_template('salary.html')

@app.route('/result', methods=["POST"])
def estimate():
    exp = request.form
    # return exp["yrs"]
    with open('model_pickle','rb') as f :
      m  = pickle.load(f)
      x=m.predict([[float(exp['yrs'])]])
      sal=x[0]
      return str(sal)

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=3080, debug=True)