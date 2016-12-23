string listOfURLs = string.Empty;

HttpWebRequest wr = (HttpWebRequest)WebRequest.Create("http://google.com");



using (HttpWebResponse response = (HttpWebResponse)wr.GetResponse())

using (Stream stream = response.GetResponseStream())

using (StreamReader reader = new StreamReader(stream))

{

    listOfURLs = reader.ReadToEnd();

}



string someUrl = listOfURLs.Substring(50, 100);



ViewBag.listofurl = listOfURLs;

return View();