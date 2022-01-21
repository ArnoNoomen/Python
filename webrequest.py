import http.client

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
    conn = http.client.HTTPConnection("ubuntu2104")
    conn.request("GET", "/")
    res = conn.getresponse()
    print(res.status, res.reason)
    data1 = res.read()
    print(data1)

if __name__ == '__main__':
    main()
