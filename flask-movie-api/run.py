from api import create_app
import os

app = create_app()

#if __name__=='__main__':
#    app.run(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))    
    #app.run(debug=True)