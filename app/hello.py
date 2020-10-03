from flask import Flask,render_template,request,url_for
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello():
    if request.method=='POST':
        dailyrate=request.form['a']
        dfm=request.form['b']
        ef=request.form['r1']
        es=request.form['d']
        hr=request.form['e']
        mr=request.form['f']
        ttlr=request.form['g']
        ycm=request.form['h']
        print(ef)
        try:
            dailyrate=int(dailyrate)
            dfm=int(dfm)
            ef=int(ef)
            es=int(es)
            hr=int(hr)
            mr=int(mr)
            ttlr=int(ttlr)
            ycm=int(ycm)
        except:
            return render_template('data.html',err_msg='Enter Valid Data')
        url = "https://7b4168uo26.execute-api.us-east-1.amazonaws.com/employee/"
        payload = " {\"data\":\"" + str(dailyrate) + ',' + str(dfm) + ',' + str(ef) + ',' + str(es) + ',' + str(hr) + ',' + str(mr) + ',' + str(ttlr) + ',' + str(ycm) + "\"" + "}"

        headers = {
            'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
            'X-Amz-Date': '20200930T095337Z',
            'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIA4KDESJFDUSSQKJSG/20200930/us-east-1/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=b81935cc533d5efb8db465da9c12f4a3ed76ca80089dfc3edebdb39df4fe5f7c',
            'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response=response.text.encode('utf8')
        response=str(response)
        print(response)
        result=response[3]
        print(result)
        if result=='N':
            return render_template('data.html',result=str(0))
        else:
            return render_template('data.html',result=str(1))
    else:
        return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
