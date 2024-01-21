Incident Report


Issue summary

From 12:04 PM South Africa standard time, requests to my airbnb clone returned a 404 error, and pages could not be found or served for users.


TIMELINE

Issue Detection:
>Time: 12:04 PM SAST 2023
> The issue was initially detected when i was testing a new feature for my airbnb clone

Actions Taken:
           >Upon detection, i initiated an investigation into my html templates because i suspected
             That maybe they were empty or had some issue that resulted in them not being read by
              The web.
           > Upon further investigation, i realized the problem was not code related, but had to do
              more with my infrastructure.

Resolution: 18:16 Dec 2023 
> A misconfigured nginx relating to the service of my web pages was identified as the      main cause of the issue.
The configuration settings were corrected, and nginx was restarted ,and after that it served pages well.

ROOT CAUSE AND RESOLUTION

ROOT CAUSE
>Nginx was not configured to serve my web pages well.
  There was a spelling error in the html page related to the pages i wanted served

RESOLUTION
> I corrected the error and made sure that nginx was correctly configured
   And that i don’t make another configuration mistake while fixing another.
   The issue was resolved when I restarted nginx.


CORRECTIVE AND PREVENTATIVE MEASURES

I regularly review nginx configurations to make sure everything is setup well.
I automate tests to verify nginx configurations before deployment
I set up monitoring alerts  to detect nginx related issues much sooner.


