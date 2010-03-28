#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


print "Content-Type: text/html";
print <<END_HTML;

<html>
<title> Flexible spreadsheet </title>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<script language="JavaScript" src="/sukhi.js"></script>
<title>Fresh Pick</title>

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
				
		<h1 id="logo-text"><a href="sheet.cgi" title="">BUGPAN Interface</a></h1>		
		<p id="slogan" >  A user friendly interface for BugPan Experiments on Locust. </p>	
		
		<div  id="nav">
			<ul>
				<li class="first" id="current"><a href="sheet.cgi">Home</a></li>
				<li><a href="blog.html">Blog</a></li>
				<li><a href="archives.html">Experiment</a></li>
				<li><a href="index.html">Support</a></li>
				<li><a href="index.html">Developers</a></li>
				<li><a href="index.html">About</a></li>		
			</ul>		
		</div>	
		
		<div id="header-image"></div>
						
	<!--header ends-->					
	</div>
