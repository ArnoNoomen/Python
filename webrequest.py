import http.client
import urllib.parse
import sys
import json

# https://docs.python.org/3/library/http.client.html#examples

#get
#request = (HttpWebRequest)WebRequest.Create(url);
#request.Method = "get";
#request.Headers["X-Oc-Restadmin-Id"] = key;
#request.ContentType = "application/json";
#response = (HttpWebResponse)request.GetResponse();
#dataStream = response.GetResponseStream();
#StreamReader sr = new StreamReader(dataStream);
#string output1 = sr.ReadToEnd();

#post
#request = (HttpWebRequest)WebRequest.Create(url);
#request.Method = "POST";
#request.Headers["X-Oc-Restadmin-Id"] = key;
#request.ContentLength = input.Length;
#request.ContentType = "application/json";
#StreamWriter sw = new StreamWriter(request.GetRequestStream());
#sw.Write(input);
#sw.Close();
#response = (HttpWebResponse)request.GetResponse();
#dataStream = response.GetResponseStream();
#StreamReader sr = new StreamReader(dataStream);
#string output1 = sr.ReadToEnd();

def main():
    webrequest_dict = {}
    try:
        with open("testbestanden/webrequest.json", encoding='iso-8859-1') as fp1:
            webrequest_dict = json.loads(fp1.read())
    except FileNotFoundError:
        print('testbestanden/webrequest.json is niet aanwezig')
        sys.exit(1)

    #params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    myheader = {'X-Oc-Merchant-Id': '123'}

    if webrequest_dict["protocol"].upper() == 'HTTPS':
        conn = http.client.HTTPSConnection(webrequest_dict["site"])
    else:
        conn = http.client.HTTPConnection(webrequest_dict["site"])
    conn.request("GET", webrequest_dict["pagina"], None, myheader)
    res = conn.getresponse()
    print(res.status, res.reason)
    data1 = res.read()
    data2 = data1.decode("utf-8")
    print(data2)

if __name__ == '__main__':
    main()
