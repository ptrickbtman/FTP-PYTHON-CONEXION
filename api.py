

#pip install  flask
from flask import Flask, jsonify, request
import dns.resolver

app = Flask(__name__)

#we define the route of the api with a parameter (data)
@app.route('/getIp/<string:url>', methods=['GET'])  

def getIp(url):
    
    #get ip of url
    result = dns.resolver.query(url, 'A')
    for ipval in result:
        ip= ipval.to_text()
    #return data in json
    return jsonify({"ip server": ip})

#localhost server up in port 5555    
if __name__ == '__main__':
    app.run(debug=True , port=5555)






