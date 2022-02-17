from main.app import app

# Telling application how and where to run application
# This is a must for Heroku deployment to work
if __name__ == "__main__":
  app.run(debug=True)
  
