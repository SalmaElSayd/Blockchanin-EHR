from unittest import result
from flask import Flask,  redirect, url_for, request,render_template
import postInitialRecord
import postVisitRecord
import getVisitRecord
import getInitialRecord
import verify_dr
import register_dr_app
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
   dr_email = request.form['dr_email']
   dr_pass = request.form['dr_pass']
   patientId = request.form['patientId']
   result = getVisitRecord.__main__(str(dr_email),str(dr_pass),str(patientId))
   res_list = result['res']
   if result['status']:
      res_list.reverse()
   return render_template('result.html', res = res_list )

@app.route('/registerHCP', methods=['POST'])
def registerHCP():
   admin_pass = request.form['admin_pass']
   admin_verified = verify_dr.__main__('admin@gmail.com',admin_pass)
   if (admin_verified):
      dr_name = request.form['dr_name']
      dr_email = request.form['dr_email']
      dr_pass = request.form['dr_pass']
      result = register_dr_app.__main__(str(dr_name), str(dr_email),str(dr_pass))
      res_list = result['res']
      return render_template('result.html', res = res_list )
   else:
      return render_template('result.html', res = "Admin password incorrect" )


@app.route('/success/<name>')
def success(name):
   return 'success : \n %s' % name

@app.route('/postInitialRecord',methods = ['POST'])
def postInitial():
   dr_email = request.form['dr_email']
   dr_pass = request.form['dr_pass']
   age = request.form['age']
   name = request.form['name']
   age = request.form['age']
   weight = request.form['weight']
   height = request.form['height']
   female = request.form['female']
   blood_pressure = request.form['blood_pressure']
   blood_glucose = request.form['blood_glucose']
   pulse = request.form['pulse']
   oxygen_level = request.form['oxygen_level']
   result = postInitialRecord.__main__(str(dr_email),str(dr_pass),str(name),int(age),int(weight),int(height),bool(female),int(blood_pressure),int(blood_glucose),int(pulse),int(oxygen_level))
   #  return redirect(url_for('success',name = name))
   return render_template('result.html', res = result['res'] )


@app.route('/postVisitRecord',methods = ['POST'])
def postVisit():
   dr_email = request.form['dr_email']
   dr_pass = request.form['dr_pass']
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
   lab_test_results = request.form['lab_test_results']
   result  = postVisitRecord.__main__(str(dr_email),str(dr_pass), str(patientId), int(age), int(weight), int(height), str(reason), str(diagnosis), str(referrals), str(follow_up), str(lab_tests), int(blood_pressure), int(blood_glucose), int(pulse), int(oxygen_level), str(lab_test_results))
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