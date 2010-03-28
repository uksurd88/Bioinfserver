#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


# decalarations
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print <<END_HTML;
<html>
<br> <!--Break to move the banner and image down-->
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
<link rel="stylesheet" href="css/lightbox.css" type="text/css" media="screen" />
<!-- wrap starts here -->
<div id="wrap">

	<!--header -->
	<div id="header">			
				
		<h1 id="logo-text"><a href="sheet.cgi" title="">BUGPAN Interface</a></h1>		
		<p id="slogan" >  A user friendly interface for BugPan Experiments on Locust. </p>	
		<div  id="nav">
			<ul id="fisheye_menu"> 
				<li class="first" id="current"><a href="home.cgi"><img src="images/home.gif" ><span>Home</span></img></a></li>
				<li><a href="sheet.cgi" onclick="Effect.SwitchOff('rolling');"><img src="images/spreadsheet.gif" ><span>Experiment</span></img></a></li>
				<li><a href="developers.cgi"><img src="images/developers.gif"><span>Developers</span></img></a></li>
				<li><a href="contactus.cgi"><img src="images/contact.gif"><span>Contact Us</span></img></a></li>		
			</ul>		
		</div>	

		 <a href="http://www.schistocerca.org/"> <div id="header-image"></div></a>
						
	<!--header ends-->					
	</div>
	<script language="JavaScript" src="fisheye.js"></script>
	<script language="JavaScript" src="lightbox.js"></script>
		<hr size='2.5'>
		<h2><center><b style='color:#008000'>The Developers </b></center></h2>
		<hr size='2.5'>
		<br><br><br><br><img src='SukhdeepSingh.png' align=right></img>
		<br><br><br><h4>Sukhdeep Singh<br>Bioinformatician<br>Masters,University of Leicester<br>United Kingdom<br> Email: vanbug\@gmail.com<br>Contact: 00447910704348<br><h4>
		<br><br><br>
		<marquee><a href="SukhdeepSingh.pdf"><input type="button" id="resume" value="Developer's Resume"></input></marquee>
		<br><br><hr size='2.5'>
END_HTML
print "<hr size='2.5'>";
