#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
# Outputs any errors to the browser window
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;

my $q = new CGI;
my $session = new CGI::Session("driver:File",$q,{Directory=>'/tmp'});
my $sid = $session->id();
my $cookie=$q->cookie(CGISESSID=>$session->id);
$sid = $q -> cookie("CGISESSID") || undef;
$session = new CGI::Session(undef,$q,{Directory=>"/tmp"});
#my $cookie;
print $q->header(-cookie=>$cookie);
# decalarations
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

# basic html starts for outputting
print "Content-Type: text/html";

print <<END_HTML;

<html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title>BugPan Interface by Sukhdeep Singh</title>
<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />
<meta name="author" content="Erwin Aligam - styleshout.com" />
<meta name="description" content="Site Description Here" />
<meta name="keywords" content="keywords, here" />
<meta name="robots" content="index, follow, noarchive" />
<meta name="googlebot" content="noarchive" />
<link rel="stylesheet" type="text/css" media="screen" href="css/screen.css" />
<body background="cake.gif"> </link>
<link type="text/css" rel="Stylesheet" href="css/blackbird.css" />
	<center>
<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
  id="welcomecurl" width="468" height="60">
  <param name="movie" value="welcomecurl.swf">
  <param name="quality" value="high">
  <param name="bgcolor" value="#FFFFFF">
  <embed name="welcomecurl" src="welcomecurl.swf" quality="high" bgcolor="#FFFFFF"
    width="468" height="60"
  </embed>
</object>
</center>

<!-- wrap starts here -->
<div id="wrap">

	<!--header -->
	<div id="header">			
				
		<h1 id="logo-text"><a href="login.cgi" title="">BUGPAN Interface</a></h1>		
		<p id="slogan" >  A user friendly interface for BugPan Experiments on Locust. </p>	
		
		<div  id="nav">
			<ul>
				<li class="first" id="current"><a href="login.cgi">Home</a></li>
				<li><a href="blog.html">Blog</a></li>
				<li><a href="sheet.cgi">Experiment</a></li>
				<li><a href="index.html">Support</a></li>
				<li><a href="index.html">Developers</a></li>
				<li><a href="index.html">About</a></li>		
			</ul>		
		</div>	
		
		<div id="header-image">
		</div>
						
	<!--header ends-->					
	</div>
<script language="JavaScript" src="/jsfile.js"></script>
<script language="JavaScript" src="/blackbird.js"></script>
<script language="JavaScript" src="/prototype.js"></script>
<script language="JavaScript" src="/scriptaculous.js"></script>
<input type="text" id="autoCompleteTextField"/>
<div id="menufield" class="autocomplete"></div>
<input type="button" id ="auto" onclick="autocomplete();">start autocomplete</input>
</head>
<!-- END DO NOT MODIFY -->
<form action="sheet.cgi" method="post">
<input type="button" name="add" value="add" onClick='ins();'></input>
<input type="submit" name="reset" value="reset"></input>
<input type="button" name="usercolumn" value="Add User Column" onClick='usercol();'></input>
<input type="button" name="save" value="Save UserFile" onClick="Effect.Appear('menufield');"></input>
<input type="button" name="statistics" value="Calculate Statistics" onClick="recalcStats();"></input>
</form>
<div id="ditto">
SHOW ME</div>
<a href=# onclick="Effect.MoveBy('ditto');"> Click me yeah Sir ji yoo</a>
<form action="download.cgi" method="post">
<input type="submit" name="statistics" value="DownLoad UserFile" id="download_button" ></input>
</form>
<table id="sessTable" border="1">
<tr id="sesRow">
<td>Session Name</td>
<td>Start Time</td>
<td>Modules Run</td>
</tr>
END_HTML

# Building Statistics
print "<div id=\"myOutput\">";
print "</div>";
print '';
print '<script language="JavaScript" type="text/javascript" src="http://pub36.bravenet.com/counter/code.php?id=407222&usernum=3046449939&cpv=2">';
print '</script>';
