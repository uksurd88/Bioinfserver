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
<form method="post" action="http://www.emailmeform.com/fid.php?formid=482603" enctype="multipart/form-data" accept-charset="UTF-8"><table cellpadding="2" cellspacing="0" border="0" bgcolor="#1980AF"><tr><td><font face="Times New Roman" size="4" color="#ffffff">BugPan Interface Contact Form</font> <div style="" id="mainmsg"> </div></td></tr></table>
<br><table cellpadding="2" cellspacing="0" border="0" bgcolor="#1980AF"><tr valign="top"> <td nowrap><font face="Times New Roman" size="4" color="#ffffff">Your Name</font></td> <td><input type="text" name="FieldData0" size="30"> </td></tr><tr valign="top"> <td nowrap><font face="Times New Roman" size="4" color="#ffffff">Your Email Address</font></td> <td><input type="text" name="FieldData1" size="30"> </td></tr><tr valign="top"> <td nowrap><font face="Times New Roman" size="4" color="#ffffff">Subject</font></td> <td><input type="text" name="FieldData2" size="30"> </td></tr><tr valign="top"> <td nowrap><font face="Times New Roman" size="4" color="#ffffff">Message</font></td> <td><textarea name="FieldData3" cols="60" rows="10"></textarea><br> </td></tr><tr valign="top"> <td nowrap><font face="Times New Roman" size="4" color="#ffffff">Upload File</font></td> 
<td><input type="file" name="FieldData4" value="" size="60"> </td></tr>
<tr> <td colspan="2"><table cellpadding=5 cellspacing=0 bgcolor="#E4F8E4" width="95%"><tr bgcolor="#1980AF"><td class="label" colspan="2"><font color="#FFFFFF" face="Verdana" size="2"><b>Image Verification</b></font></td></tr><tr><td class="captcha" style="padding: 2px;" width="10"><img src="http://www.emailmeform.com/turing.php" id="captcha" alt="captcha"></td><td class="field" valign="top">
<div><font color="#000000">Please enter the text from the image</font>:<br><input type="text" name="Turing" value="" maxlength="100" size="10"> [ <a href="#" onclick=" document.getElementById('captcha').src = document.getElementById('captcha').src + '?' + (new Date()).getMilliseconds()">Refresh Image</a> ] [ <a href="http://www.emailmeform.com/?v=turing&pt=popup" onClick="window.open('http://www.emailmeform.com/?v=turing&pt=popup','_blank','width=400, height=500, left=' + (screen.width-450) + ', top=100');return false;">What's This?</a> ]</div></td></tr></table></td></tr><tr> <td> </td> <td align="right"><input type="text" name="hida2" value="" maxlength="100" size="3" style="display : none;"><input type="submit" class="btn" value="Submit" name="Submit">    <input type="reset" class="btn" value="  Clear  " name="Clear"></td></tr><tr><td colspan=2 align="center"><br></td></tr></table></form>
END_HTML
print "<hr size='2.5'>";
