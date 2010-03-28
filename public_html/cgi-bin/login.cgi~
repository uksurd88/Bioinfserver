#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard :html3);

# basic html starts for outputting
print "Content-Type: text/html";
print <<END_HTML;

<html>
<title> Flexible spreadsheet </title>
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

<!-- wrap starts here -->
<div id="wrap">

	<!--header -->
	<div id="header">			
				
		<h1 id="logo-text"><a href="login.cgi" title="">BUGPAN Interface</a></h1>		
		<p id="slogan" >  A user friendly interface for BugPan Experiments on Locust. </p>	
		
		<div id="header-image"></div>
		<script language="JavaScript" src="/jsfile.js"></script>
		<script language="JavaScript" src="/prototype.js"></script>
		<script language="JavaScript" src="/scriptaculous.js"></script>				
	<!--header ends-->					
	</div>
<center>
<form action="sheet.cgi" method="post">
<div style="text-align: right; width:210px; padding:5px;">
    <div style="padding:3px; font: bold 13px arial;">Enter Password Protected Area</div>
    <div style="padding:3px; font: normal 13px arial;">Username: <input type="text" id="uname" size="15" maxlength="30" style="width: 100px"></div>
    <div style="padding:3px; font: normal 13px arial;">Password: <input type="password" id="passwd" size="15" maxlength="30" style="width: 100px" onMouseOver="details();"></div>
    <div style="padding:3px;"><a style="font: bold 11px arial;" href='mailto: Sukhdeep Singh <vanbug\@gmail.com>'>Request Password</a> &nbsp; <input type="submit" name="submit" value="Login" style="width: 65px;" onClick="details();"></div>
    <div style="padding:5px; font: normal 11px arial;"><a href="#">Powered by Sukhdeep Singh</a></div>
</div>
</center>
</form>
</div>

END_HTML

