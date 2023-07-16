from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {'id': 1,
    'title': 'Manager',
    'location': 'London',
    'salary': '$40k'
  },
  
   {'id': 2,
    'title': 'Receptionist',
    'location': 'Hull',
   },
  
   {'id': 3,
    'title': 'Warehouse worker',
    'location': 'Manchester',
    'salary': '$30k'
   }
  
]

@app.route("/")
def activate_website():
    return render_template('home.html',
                           listing=JOBS,
                          )

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)