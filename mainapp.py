from flask import Flask, render_template, request, session
import logging
import os

from google.cloud import storage

#from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

def uploadfile(bucketname, filefrom, fileto):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucketname)
    senddata = bucket.blob(fileto)
    senddata.upload_from_filename(filefrom)




@app.route('/', methods=['GET', 'POST'])
def choosesport(): 
    return render_template("index.html")
    


@app.route('/result', methods=['GET', 'POST'])
def kamal():
    x = render_template("result.html", sport= request.form['sport'])
    y = x.split()
    word = str(y[21])
    f = open("transferme.txt", "a")
    f.write(word + "\n")
    f.close()
    uploadfile("reliable-bruin-323211_cloudbuild","transferme.txt","transferme.txt")
    return render_template("result.html", sport= request.form['sport'])
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
