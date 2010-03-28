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
my $everyline;
my $i=0;
my $session;
my @session;
my @ecVoltage;
my @show;
my $start;
my @start;
my @start1;
my $match;
my @module;
my $count;
# writing sessions list to a file locally
system("bugsess list >/tmp/sessions.txt");

# basic html starts for outputting
print "Content-Type: text/html\n\n";
print <<END_HTML;

<html>
<title> Flexible spreadsheet </title>


<!-- Commenting some lines
<form action="ask.cgi" method="post">
<input type="text" name="query" value="Query" id="queryString">
<input type="button" name="ask" value="Ask" onclick="askQuery()">
</form>
<div id="showSession"></div>
<div id="showQuery"></div>
</body>
</html>
--!>

<script language="JavaScript" src="/prototype.js"></script>
<script language="JavaScript" src="/jsfile.js"></script>
<input type="button" name="add" value="add" onClick='ins();'></input>
<form action="sheet.cgi" method="post">
<input type="reset" name="reset" value="reset"></input>
</form>
<table id="sessTable" border="1">
<tr id="sesRow">
<td>Session Name</td>
<td>Start Time</td>
<td>Modules Run</td>
</tr>
END_HTML


@buglist = `bugsess list -m`;

foreach $line (@buglist)
{
$line =~ /(\w{1,6})/;
$session[$i]=$1;

@show = `bugsess show $1`;
system("bugsess show $1 >>/tmp/show.txt");
foreach $everyline (@show)
{
if($everyline =~ /^Start\stime:\s\w+\s(\w+\s+\d+\s+)\d+\W+\d+\W\d+\s+\w+(\s+\d+.+)/mgis) {
  $start[$i]=$1;
  $start1[$i]=$2;
}
if($everyline =~ /^Modules\s\w+\W(.+)/) {
     $module[$i]=$1;
}
}
print '<tr id="sessRow'.$i.'">';
print '<td id="sessNm'.$i.'">'.$session[$i].'</td>';
print '<td id="sessDt'.$i.'">'.$start[$i].$start1[$i].'</td>';
print '<td id="sessMd'.$i.'">'.$module[$i].'</td>';
print "</tr>";
$i++;
$count=$i;
}
print "</table>";
#print <<END_HTML;

#END_HTML

# Javascript starting for fetching session names and declaring some global variables
print '<script language="JavaScript">';
print "var count=$count;";
print "var colcount=0;";
print "var i=0;";
print "var sessionName=[];";
for ($i=0;$i<$count;$i++) {
print "sessionName[$i]=\"" . $session[$i] . "\";\n";
			}
print "</script>";
print '<div id="temp"></div>';
print "</body>";
print "</html>";