#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


# decalarations
my @buglist;
my $infile = "/tmp/sessions.txt";
my $line;
my $i=0;
my $session;
my @session;
my @ecVoltage;
system("bugsess list >/tmp/sessions.txt");
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print "<html>";
print '<head> <script language="JavaScript" src="/prototype.js"></script>';
print '<script language="JavaScript" src="/sukhi.js"></script>';
print "</head>";
print "<body>";
print "Current Sessions  ";
print '<form action="ask.cgi" method="post">';
print '<select name="session" id="sessionchooser" onchange="changeSession()">';
@buglist = `bugsess list`;
foreach $line (@buglist)
{
$line =~ /(\w+)/;
print "<option value=$1>" . $1 . "</option>";
$session[$i]=$1;
$i++;
}

print "</select>";
print <<END_HTML;
<input type="text" name="query" value="Query" id="queryString">
<input type="button" name="ask" value="Ask" onclick="askQuery()">
</form>
<div id="showSession"></div>
<div id="showQuery"></div>
</body>
</html>
END_HTML
#@ecVoltage='bugsess ask1 '.$1.'ecVoltage';
