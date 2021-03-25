
from flask import Flask, url_for, jsonify , request,json
import string

from datetime import datetime
from app_key import require_appkey

import csv
import os
import random
import linecache


import sys
if sys.version_info.major < 3:
    reload(sys)




app = Flask(__name__)
csv.field_size_limit(sys.maxsize)


#@app.before_first_request





 


@app.route('/api')
@require_appkey
def sentimentAnalysisV2():
 try: 
  nom= request.json['nom']
 
  return jsonify ({'msg': "hello"+nom })
   

  
 except:
     return jsonify ({'msg': "erreur", })





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='4000')