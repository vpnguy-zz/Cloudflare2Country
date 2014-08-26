#CloudFlare to Country
###by DaRkReD

---
####Usage:

```python
python CloudFlare2Country.py
```
####Dependencies:

[pandas] - Used for datastructure and csv manipulation

---
##Writeup

###Introduction
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The http protocol has risen in dominance as malware's command and control protocol of choice. Therefore, it has become standard operating procedure for cyber criminals to hide behind CloudFlare. They do this to prevent both denial of service attacks and preserve anonymity of the hosting provider to avoid legal actions (DMCA and Malware Reports). CloudFlare provides security by obscurity to hide the true IP of the server.

####Current Methods
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A number of techniques currently exist to "*resolve*" CloudFlare with the two most popular being broad IP scanning and services which leak the server IP.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Broad IP scanning is the process of scannin gentire IP ranges for servers which return the content that CloudFlare is protecting. This method is extremely slow by nature as it has to scan the entire internet looking for a chunk of matching data.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By default, CloudFlare enables __*direct.website.com*__ which bypasses the CloudFlare CDN thus providing the true server IP. Most cyber criminals will disable this instantly to prevent this type of IP leak. Other subdomains such as __*ftp.website.com*__ that need to allow FTP traffic can also cause an IP leak.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additionally, services running on the server may also compromise the IP address. For example a mail server on __*website.com*__ sends an email to a user informing them of a password reset. Often, due to misconfigurations and default configurations, the email header region often contains the real IP of __*website.com*__. This is due to the mail server not being setup to use __*website.com*__. Instead the mail server uses the servers IP address and discloses it to anyone receiving mail from the server. Mitigation of the service level leaks include using 3rd party mail providers and disabling services.

###Cloudflare2Country Method
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;While CloudFlare's CDN provides acceleration and caching for http content, a small difference in the maximum and minimum latency can indicate the host country of any IP cloaked by CloudFlare with relative accuracy. Ping deviation can be established using a plethora online multi-ping tools such as [cloudmonitor.ca.com](http://cloudmonitor.ca.com/en/ping.php "CA Multiping") which pings the target from 90 locations. With 90 locations worth of data it is possible to isolate a CloudFlare server to its country of origin and thus enhance the accuracy of Broad IP scanning and reduce the time it takes to scan for a given target.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The attached script uses sample data from a server behind CloudFlare physically located in the Czech Republic. When ran the script will perform an analysis of the ping results and find the country in which the server resides.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;While it is possible to automate the process of querying a multi-ping service it was decided to not restrict users to an individual query service.