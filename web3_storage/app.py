from unittest import result
from flask import Flask,  redirect, url_for, request,render_template
import postInitialRecord
import postVisitRecord
import getVisitRecord
import getInitialRecord
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html',res="" )

# @app.route('/readInitial', methods = ['POST'])
# def getInitialVisit():
#    patientId = request.form['patientId']
#    res = getInitialRecord.__main__(int(patientId))
#    return  redirect(url_for('success',name = res))

@app.route('/readVisit', methods=['POST'])
def getVisit():
   patientId = request.form['patientId']
   result = getVisitRecord.__main__(int(patientId))
   res_list = result['res']
   if result['status']:
      res_list.reverse()
   return render_template('result.html', res = res_list )

@app.route('/success/<name>')
def success(name):
   return 'success : \n %s' % name

@app.route('/postInitialRecord',methods = ['POST'])
def postInitial():
    name = request.form['name']
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']
    female = request.form['female']
    blood_pressure = request.form['blood_pressure']
    blood_glucose = request.form['blood_glucose']
    pulse = request.form['pulse']
    oxygen_level = request.form['oxygen_level']
    result = postInitialRecord.__main__(str(name),int(age),int(weight),int(height),bool(female),int(blood_pressure),int(blood_glucose),int(pulse),int(oxygen_level))
   #  return redirect(url_for('success',name = name))
    return render_template('result.html', res = result['res'] )


@app.route('/postVisitRecord',methods = ['POST'])
def postVisit():
    patientId = request.form['patientId']
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']

    reason =request.form['reason']
    diagnosis =request.form['diagnosis']
    referrals =request.form['referrals']
    follow_up =request.form['follow_up']
    lab_tests =request.form['lab_tests']

    blood_pressure = request.form['blood_pressure']
    blood_glucose = request.form['blood_glucose']
    pulse = request.form['pulse']
    oxygen_level = request.form['oxygen_level']
    result  = postVisitRecord.__main__(int(patientId), int(age), int(weight), int(height), str(reason), str(diagnosis), str(referrals), str(follow_up), str(lab_tests), int(blood_pressure), int(blood_glucose), int(pulse), int(oxygen_level))
   #  return redirect(url_for('success',name = hash))
    return render_template('result.html', res = result['res'] )


# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


if __name__ == '__main__':
   app.run(debug=True)