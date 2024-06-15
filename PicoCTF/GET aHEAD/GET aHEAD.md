Description
Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:15931/



Hint 1: Maybe you have more than 2 choices
Hint 2: Check out tools like Burpsuite to modify your requests and look at the responses


Looking through the source code, I learnt that the website sent data not using parameters, but the request type, as GET requests and POST requests were used to show the red and blue sections of the website respectively.

I used Google Chrome's Developer tools to extract the web request, and imported it into Insomnia. After this, I was able to send requests of every type desirable.

After going through every request type listed by default in insomnia, the HEAD request resulted in no body returned from the request, however after looking in the headings, the flag was revealed: 

>! 	picoCTF{r3j3ct_th3_du4l1ty_82880908}

Brute forcing was not neccessary as HEAD was highlighted in the problem name, and could have been jumped to from there.