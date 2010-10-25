#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);
my $modeller;
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print "<html>\n";
print "<head>\n";
print "<title>Modeller </title>\n";
print "</head>\n\n";
print "<h2> <center> \n Welcome to Modeller page </center> </h2>";
print "<body>\n\n";

print ("<br>Please wait while modeller is running...<br>");
# running modeller
print ("<br>You can view report when the loading has stopped.<br>");
print <<END_HTML;
<html>
<body>
<form action="run.log" method="post">
<input type="radio" name="radio" value="modeller"$modeller> Modeller Report
</p>
<input type="submit" name="go" value="View">
</form>
<form><input type="button" value="Download Model1" onClick="window.location.href='http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/model.B99990001.pdb'"></form>
<form><input type="button" value="Download Model2" onClick="window.location.href='http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/model.B99990002.pdb'"></form>
<form><input type="button" value="Download Model3" onClick="window.location.href='http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/model.B99990003.pdb'"></form>
<form><input type="button" value="Download Model4" onClick="window.location.href='http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/model.B99990004.pdb'"></form>
<form><input type="button" value="Download Model5" onClick="window.location.href='http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/model.B99990005.pdb'"></form>
<form><input type="button" value="View Best Model" onClick="window.location.href='http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/1W5Y.png'"></form>

</body>
</html>
END_HTML
#running pymol in command line
#system ("pymol -c");
system("/usr/bin/mod9v4 run.py");
print "<HR>";
print "<marquee><font face=andy><br><br><br><br><br><br><br><br> Created by <b>Sukhdeep Singh</b> Webmodeller v 1.0</font></marquee>";
print "</body>\n";
print "</html>\n";
