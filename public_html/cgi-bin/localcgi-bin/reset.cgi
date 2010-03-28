#!/usr/bin/perl
########################################################################################
########################################################################################
################################# # B U G P A N -  I N T E R F A C E###################################
########################################################################################
########################################################################################
# loading usual development settings using CGI module
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
# Outputs any errors to the browser window
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;

########################################################################################
########################################################################################
## Some work on generating cookies and specific id and generating sessions for the user remembrance
my $q = new CGI;
my $session = new CGI::Session("driver:File",$q,{Directory=>'/tmp'});
my $sid = $session->id();
my $cookie=$q->cookie(CGISESSID=>$session->id);
$sid = $q -> cookie("CGISESSID") || undef;
$session = new CGI::Session(undef,$q,{Directory=>"/tmp"});
#my $cookie;
print $q->header(-cookie=>$cookie);
########################################################################################
########################################################################################
#  All decalarations are defined here
	my $username = $q-> param('username');
	my $useroutput = $q -> param('useroutput');
	my $filename = $q -> param('filename');
	my @buglist;
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
	my $numberofRows;
	my $files;
	my @files;
	my $var;
# basic html starts for outputting
print "<div id='top'>";
print "Content-Type: text/html";
########################################################################################
########################################################################################
## All html and javascript for sheet.cgi is contained between these END_HTML identifiers
########################################################################################
print <<END_HTML;

<html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<div id="main">
<title>BugPan Interface by Sukhdeep Singh</title>
<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />
<meta name="author" content="Erwin Aligam - styleshout.com" />
<meta name="description" content="Site Description Here" />
<meta name="keywords" content="keywords, here" />
<meta name="robots" content="index, follow, noarchive" />
<meta name="googlebot" content="noarchive" />
<link rel="stylesheet" type="text/css" media="screen" href="css/screen.css" />
<link type="text/css" rel="Stylesheet" href="css/blackbird.css" />
<link rel="stylesheet" href="css/proto.menu.0.6.css" type="text/css" media="screen" />
<link rel="stylesheet" type="text/css" href="css/fisheye-menu.css" />
<!-- wrap starts here -->
<div id="wrap">

	<!--header -->
	<div id="header">			
				
		<h1 id="logo-text"><a href="sheet.cgi" title="">BUGPAN Interface</a></h1>		
		<p id="slogan" >  A user friendly interface for BugPan Experiments on Locust. </p>	
		<div  id="nav">
			<ul id="fisheye_menu"> 
				<li class="first" id="current"><a href="login.cgi"><img src="images/home.gif" ><span>Home</span></img></a></li>
				<li><a href="sheet.cgi" onclick="Effect.SwitchOff('rolling');"><img src="images/spreadsheet.gif" ><span>Experiment</span></img></a></li>
				<li><a href="index.html"><img src="images/developers.gif"><span>Developers</span></img></a></li>
				<li><a href="index.html"><img src="images/contact.gif"><span>Contact Us</span></img></a></li>		
			</ul>		
		</div>	

		 <a href="http://www.schistocerca.org/"> <div id="header-image"></div></a>
						
	<!--header ends-->					
	</div>
	<div id="rolling">
<!--<center>	<h3>Welcome $username to BugPan Interface.</h3></center>-->
<script language="JavaScript" src="/jsfile.js"></script>
<script language="JavaScript" src="/blackbird.js"></script>
<script language="JavaScript" src="/prototype.js"></script>
<script language="JavaScript" src="/proto.menu.0.6.js"></script>
<script language="JavaScript" src="/protomenu.js"></script>
<script language="JavaScript" src="/scriptaculous.js"></script>
<script language="JavaScript" src="/effects.js"></script>
<script language="JavaScript" src="/sheetmigration.js"></script>
<script language="JavaScript" src="/fisheye.js"></script>
		<!--<input type="text" id="autoCompleteTextField"/>
		<div id="menufield" class="autocomplete"></div>
		<input type="button" onclick="autocomplete();">start autocomplete</input>
		-->
		</head>
				<form action="sheet.cgi" method="post">
				<input type="button" name="add" value="Add" onClick='ins();'></input>
				<input type="submit" name="reset" value="Reset"></input>
				<input type="button" name="usercolumn" value="Add User Column" onClick='usercol();'></input>
				<input type="button" name="save" value="Save UserFile" onClick='saving();'></input>
				<input type="button" name="statistics" value="Calculate Statistics" onClick="recalcStats();"></input>
				<input type="submit" name="statistics" value="DownLoad UserFile" id="download_button" onclick="renew();"></input>
				</form>
				&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
				<a onclick="Effect.Grow('renew');"><b style="color:green">Show Sheet |</b></a>
				<a onclick="Effect.SwitchOff('renew');"><b style="color:green">Hide Sheet |</b></a>
				<a onclick="Effect.Grow('userfiles');"><b style="color:green">Show UserFiles |</b></a>
				<a onclick="Effect.SwitchOff('userfiles');"><b style="color:green">Hide UserFiles </b></a>
				<input type="text" value="filter values" id="renewbox" onChange="renew();" > <b><input type="button" value="?" onClick="popup1()";></b></input>
END_HTML

########################################################################################
########################################################################################
## picking all usersaved text files from /tmp/usersheets/
@files = `ls /var/usersheets/*.txt`;
print "<div id='userfiles'>";
print "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<b>Browse User Files</b> ";
print "<select id=\"download_chooser\" onChange=\"downloading();\">";
foreach $files(@files)
{
$files =~/^\/\w+\/\w+\/(.+)/;
print "<option value=$1>$1</option>";
}
print "</select>";
print "</div>";
########################################################################################
########################################################################################
# Generates the sheet on the browser window
# Gives the session list  
print '<div id="renew">
							<table  onMouseover="changeto(event, \'lightgreen\')" onMouseout="changeback(event, \'#3999ee\')" onClick="selectcell(event)"  								id="sessTable" border="1" >
							<tr id="sesRow" >
							<td id="ignore"><b>Session Name</b></td>
							<td id="ignore"><b>Start Time</b></td>
							<td id="ignore"><b>Modules Run</b></td>
							</tr>
							</div>';
							
@buglist = `bugsess list -m  2>/dev/null`;

foreach $line (@buglist)
{
$line =~ /(\w{1,6})/;
$session[$i]=$1;

@show = `bugsess show $1 2>/dev/null`;
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
print '<td id="name'.$i.'">'.$session[$i].'</td>';
print '<td id="date'.$i.'">'.$start[$i].$start1[$i].'</td>';
print '<td id="mode'.$i.'">'.$module[$i].'</td>';
print "</tr>";
$i++;
$numberofRows=$i;
}
########################################################################################
########################################################################################
## Generates the Statistics cells viz, mean and standard deviation
		print '<tr id="MeanRow">';
		print '<td id="mean0">Mean</td>';
		print '<td id="mean1">Mean</td>';
		print '<td id="mean2">Mean</td>';
		print '</tr>';
		print '<tr id="stdevrow">';
		print '<td id="stdv0">Standard Deviation</td>';
		print '<td id="stdv1"></td>';
		print '<td id="stdv2"></td>';
		print "</tr>";
		print "</table>";
## renew id finishes
#print "</div>";
#table finishes
########################################################################################
########################################################################################
print '<div id="load"/>';
# Javascript starting for fetching session names and declaring some global variables
	print '<script language="JavaScript">';
	print "var numberofRows=$numberofRows;";
	print "document.onkeypress=migrate;";
	print "var colcount=0;";
	print "var i=0;";
	print "var sessionName=[];";
			for ($i=0;$i<$numberofRows;$i++) 
			{
			print "sessionName[$i]=\"" . $session[$i] . "\";\n";
				}
	print "new Proto.Menu({
	  selector: '#renew', 
	  className: 'menu desktop', 
	  menuItems: myMenuItems
	})";
	print "</script>";

# New division for Ajax Outputting
print "<div id=\"myOutput\"/>";
print "</div>";
# Counter by bravenet for bugpan
#print '<script language="JavaScript" type="text/javascript" src="http://pub36.bravenet.com/counter/code.php?id=407222&usernum=3046449939&cpv=2">';
#print '</script>';
# division main ends here
print "</div>";
print '<hr size=2.5>';
print "<div id='detailask'> </div>";
print "</div>"; # Ending top division
#print '<h5><div onmouseover="popup2();"><font color="Orange"><MARQUEE>Developed by <b><i>Sukhdeep Singh</b></i></MARQUEE></font></div></h5>';
########################################################################################
########################################################################################
########################################################################################
################################# DEVELOPER : SUKHDEEP SINGH###################################
########################################################################################
########################################################################################
########################################################################################
########################################################################################
