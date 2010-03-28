#!/usr/bin/perl

# loading usual development settings/
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


# decalarations
my $q = new CGI;
my $session = $q -> param('session');
our $date;
my @bugshow;
my $line;
@bugshow = `bugsess show $session`;
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
				<li><a href="index.html"><img src="images/developers.gif"><span>Developers</span></img></a></li>
				<li><a href="index.html"><img src="images/contact.gif"><span>Contact Us</span></img></a></li>		
			</ul>		
		</div>	

		 <a href="http://www.schistocerca.org/"> <div id="header-image"></div></a>
	<script language="JavaScript" src="fisheye.js"></script>
	<!--header ends-->					
	</div>

<!-- HOME page introduction starts here -->
 <hr size="1">
<p><font color="green">
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
	<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
	<TITLE>TITLE</TITLE>
	<META NAME="GENERATOR" CONTENT="OpenOffice.org 2.4  (Linux)">
	<META NAME="AUTHOR" CONTENT="Sukhdeep Singh">
	<META NAME="CREATED" CONTENT="20091120;11560000">
	<META NAME="CHANGEDBY" CONTENT="Sukhdeep Singh">
	<META NAME="CHANGED" CONTENT="20091124;16262200">
	<STYLE TYPE="text/css">
	<!--
		@page { margin-right: 1.5cm; margin-top: 2cm; margin-bottom: 2cm }
		P { margin-bottom: 0.21cm; direction: ltr; color: #000000; widows: 0; orphans: 0 }
		P.western { font-family: "Times New Roman", serif; font-size: 12pt }
		P.cjk { font-family: "DejaVu Sans", "Times New Roman"; font-size: 12pt }
		P.ctl { font-family: "DejaVu Sans", "Times New Roman"; font-size: 12pt; so-language: en-US }
		H1 { margin-bottom: 0.11cm; direction: ltr; color: #000000; widows: 0; orphans: 0 }
		H1.western { font-family: "Arial", sans-serif; font-size: 16pt }
		H1.cjk { font-family: "DejaVu Sans", "Times New Roman"; font-size: 16pt }
		H1.ctl { font-family: "Arial", sans-serif; font-size: 16pt; so-language: en-US }
		H2 { margin-bottom: 0.11cm; direction: ltr; color: #000000; widows: 0; orphans: 0 }
		H2.western { font-family: "Arial", sans-serif; font-size: 14pt; font-style: italic }
		H2.cjk { font-family: "DejaVu Sans", "Times New Roman"; font-size: 14pt; font-style: italic }
		H2.ctl { font-family: "Arial", sans-serif; font-size: 14pt; so-language: en-US; font-style: italic }
		H3 { margin-bottom: 0.11cm; direction: ltr; color: #000000; widows: 0; orphans: 0 }
		H3.western { font-family: "Arial", sans-serif; font-size: 13pt }
		H3.cjk { font-family: "DejaVu Sans", "Times New Roman"; font-size: 13pt }
		H3.ctl { font-family: "Arial", sans-serif; font-size: 13pt; so-language: en-US }
		H4 { margin-bottom: 0.21cm; direction: ltr; color: #000000; widows: 0; orphans: 0 }
		H4.cjk { font-family: "DejaVu Sans", "Times New Roman" }
		H4.ctl { font-family: "DejaVu Sans", "Times New Roman"; so-language: en-US }
	-->
	</STYLE>
</HEAD>
<BODY LANG="en-GB" TEXT="#000000" BGCOLOR="#ffffff" DIR="LTR">
<DIV TYPE=HEADER>
	<P STYLE="margin-bottom: 0.9cm"><FONT COLOR="#b3b3b3"><U>BUGPAN
	INTERFACE</U></FONT><U>		</U><FONT COLOR="#7f7f7f"><U>Page</U></FONT><U>
	| <SDFIELD TYPE=PAGE SUBTYPE=RANDOM FORMAT=PAGE>42</SDFIELD></U></P>
</DIV>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<IMG SRC="TheBugPanInterfacet_html_282087c6.jpg" NAME="graphics1" ALIGN=BOTTOM WIDTH=300 HEIGHT=71 BORDER=0></P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<FONT SIZE=4><B>BUGPAN INTERFACE</B></FONT></P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
A STRUCTURED SPREADSHEET WEB INTERFACE</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
FOR NEUROPHYSIOLOGY ANALYSIS</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
By</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
SUKHDEEP SINGH</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
B. Tech</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
Kurukshetra University</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
2008</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
A Dissertation</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
Submitted in Partial Fulfilment of the Requirements for the</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
Masters of Science</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
Bioinformatics</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
Department of Biochemistry</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
University of Leicester UK</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
November 2009</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<H1 CLASS="western" ALIGN=CENTER STYLE="page-break-before: always"><A NAME="1.ABSTRACT|outline"></A>
<FONT FACE="Times New Roman, serif">ABSTRACT</FONT></H1>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
With advances in technology, there is an increase in research all
around the world. Increase in research implies increased
experimentation, leading to a huge amount of data generation causing
data analysis problems as a result of lack of resources and
knowledge. Present data analysis software packages are complex,
require expensive licensing and have data format problems. In
practice, most scientists use simple spreadsheets but these also
imposes constraints on data views and cause file handling problems.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
A solution to this problem is developing a web graphical user
interface, which allows experimentation and data analysis on the same
platform, thus removing the data input problem. Developing it on the
web enables the remote access. This motivated us to develop a web
interface which improves scientific data analysis problems.
Currently, it has been implemented for neurophysiology experiments as
a test subject. The data generated by each experiment are analysed as
a spreadsheet grid where rows represent experiments and columns
display the query results. Users can represent data in the form of
graphs (histograms, ‘xy’ scatter plots), tables, or as raw output
generated by the program.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
The structure is being built on Ajax, which allows fast and efficient
data retrieval with minimal consumption of resources. It removes the
submit-wait paradigm and allows quick server response. For
spreadsheet simulation within the web interface, sheet navigation
with keyboard is also being defined, displaying different data
representations for each selected cell.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
The BugPan interface is an effort to add a resource to the world of
data management. It is simple but very powerful allowing scientists
to carry out experiments along with data analysis in a well
structured manner on the web from any part of the world using new
technologies.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
The BugPan Interface can be accessed through the University of
Leicester’s web server at
http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/home.cgi.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
	</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B>TABLE
OF CONTENTS</B></U></FONT></P>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<DIV ID="Table of Contents1" DIR="LTR">
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#1.ABSTRACT|outline">ABSTRACT	2</A></B></U></FONT></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#2.1. INTRODUCTION|outline">1.
	INTRODUCTION	4</A></B></U></FONT></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#2.1.1.1 NEUROBIOLOGY – THE SCIENCE OF BRAINS|outline">1.1
	NEUROBIOLOGY – THE SCIENCE OF BRAINS	5</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#2.2.1.2 THE NEUROPHYSIOLOGY EXPERIMENT|outline">1.2
	THE NEUROPHYSIOLOGY EXPERIMENT	6</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#2.3.1.3 DEVELOPMENT OF A LANGUAGE FOR DEFINING EXPERIMENTS|outline">1.3
	DEVELOPMENT OF A LANGUAGE FOR DEFINING EXPERIMENTS	9</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#2.4.1.4 AIM OF THE Project|outline">1.4
	AIM OF THE Project	11</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#2.5.1.5 Questions Developing BugPan Interface|outline">1.5
	Questions Developing BugPan Interface	11</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#2.6.1.6 WHY USE a WEB INTERFACE_|outline">1.6
	WHY USE a WEB INTERFACE?	13</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#2.7.1.7 Statement of the problem|outline">1.7
	Statement of the problem	13</A></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#3.2. METHODOLOGY|outline">2.
	METHODOLOGY	15</A></B></U></FONT></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#3.1.2.1 BugPan Interface System Architecture (GUI)|outline">2.1
	BugPan Interface System Architecture (GUI)	15</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#3.2.2.2 BugPan System Architecture (CLI)|outline">2.2
	BugPan System Architecture (CLI)	15</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#3.3.2.3 Programming Platforms|outline">2.3
	Programming Platforms	16</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#3.4.2.4 Servers used|outline">2.4
	Servers used	18</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#3.5.2.5 Editors useD|outline">2.5
	Editors useD	19</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#3.6.2.6 Debuggers used|outline">2.6
	Debuggers used	19</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#3.7.2.7 Statistical Software used|outline">2.7
	Statistical Software used	19</A></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#4.3 RESULTS|outline">3
	RESULTS	20</A></B></U></FONT></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#4.1.3.1 DEVELOPMENT OF THE BUGPAN INTERFACE|outline">3.1
	DEVELOPMENT OF THE BUGPAN INTERFACE	20</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#4.2.3.2 BUGPAN INTERFACE FRAMEWORK|outline">3.2
	BUGPAN INTERFACE FRAMEWORK	20</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#4.3.3.3 BUGPAN LAYOUT|outline">3.3
	BUGPAN LAYOUT	25</A></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#5.4. DISCUSSION|outline">4.
	DISCUSSION	27</A></B></U></FONT></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#5.1.TESTING Hypothesis|outline">TESTING
	Hypothesis	27</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#5.2.CHALLENGING CURRENT DEVELOPMENTS|outline">CHALLENGING
	CURRENT DEVELOPMENTS	28</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#5.3.FUTURE SCOPE|outline">FUTURE
	SCOPE	30</A></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#7.5. CONCLUSION|outline">5.
	CONCLUSION	31</A></B></U></FONT></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#8.6. ACKNOWLEDGEMENTS|outline">6.
	ACKNOWLEDGEMENTS	32</A></B></U></FONT></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#9.7. BIBLIOGRAPHY|outline">7.
	BIBLIOGRAPHY	33</A></B></U></FONT></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B><A HREF="#10.8. APPENDICES|outline">8.
	APPENDICES	36</A></B></U></FONT></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#10.1.APPENDIX I|outline">APPENDIX
	I	36</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#10.2.APPENDIX II|outline">APPENDIX
	II	37</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#10.3.APPENDIX III|outline">APPENDIX
	III	38</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#10.4.APPENDIX IV|outline">APPENDIX
	IV	39</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#10.5.APPENDIX v|outline">APPENDIX
	v	40</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#10.6.APPENDIX vi|outline">APPENDIX
	vi	41</A></P>
	<P STYLE="margin-left: 0.42cm; margin-bottom: 0cm"><A HREF="#10.7.APPENDIX vii|outline">APPENDIX
	vii	42</A></P>
</DIV>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<FONT SIZE=3 STYLE="font-size: 11pt"><U><B>INDEX OF TABLES</B></U></FONT></P>
<DIV ID="Illustration Index1" DIR="LTR">
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B>Table
	1.Contrast between Graphical User Interface and Command Line
	Interface.	12</B></U></FONT></P>
	<P STYLE="margin-bottom: 0cm"><FONT SIZE=3 STYLE="font-size: 11pt"><U><B>Table
	2 Table representing different output possibilities for different
	data types and value counts.	22</B></U></FONT></P>
</DIV>
<H1 CLASS="western" STYLE="page-break-before: always"><FONT FACE="Times New Roman, serif">1.
INTRODUCTION</FONT></H1>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Experimentation is the building block of scientific inventions and
discoveries. Every successful invention is linked to a number of
repeatable experiments behind it, generating a vast amount of data
which is sometimes difficult to analyse and process by the
experimenter himself. Uncountable numbers of experiments are being
done on a large scale in different fields globally every day, whose
analysis is often complicated as compared to data generation, and as
a result, scientists are not able to fully analyse their data which
leads to missed opportunities. 
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
		Every software package requires some knowledge to operate it, but
among them, some require more specialist knowledge than others. Data
analysis software plays a very important role in calculating
statistics for the data, making graphical representations and linking
data, but can be complicated and costly as well as requiring
extensive knowledge and licensing. In addition, SQL (Structured Query
Language) (Jamison 2003) databases often require proper database
management professionals to ensure adequate performance for
retrieving information. For a scientific professional such as a
researcher conducting a bio-chemical experiment, who is generating
large datasets on an everyday basis, it can be very difficult to use
statistical software and databases.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
		Various measures have been proposed for inspecting, visualising and
annotating large datasets from databases, but in practice most
scientists use a plain spreadsheet to analyse and store data.
Spreadsheets take the form of a grid where data can be written,
stored and analysed, and users can also construct graphs, apply
mathematical functions and calculate statistics such as mean, median
etc. This approach is practical because it imposes almost no
constraints but it has a number of disadvantages as there are no
checks on the integrity of the data. Also, it is difficult to change
the shape of the sheet for different views of the data, and the data
has to be entered manually or imported from different sources and
applications, which is actually time consuming and error-prone
(Augustsson<I> et al.</I> 2008)</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
		Almost all spreadsheet packages work the same way by calculating
numeric data and making statistical models. They help in organizing
and sharing data with simulating reality of working on a paper grid. 
The simple spreadsheet helps in numerous ways as it’s easy to use
and learn, and the data can be analysed frequently without
complications, but this too has problems such as:</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	The data needs some importing and exporting, every time an
	experiment is done.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	The user has to have some knowledge of working on spreadsheet so as
	to use complex functions, creating sophisticated charts and graphs.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	 If there is some error in data, the user has to run the experiment
	again and import the data again for analysis. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Importing and exporting can sometimes cause a copy error which can
	lead to incorrect analysis. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Last but not the least; it is difficult to work interactively with
	remote collaborators.</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Experimenting is the core of science and these days the rush is for
exceptional data analysis methods which allow deep investigation of
data along with error reporting and troubleshooting properties. This
data analysis problem is worse in multidisciplinary fields such as
Neuroscience which deals with a wide range of problems such as how
brains evolved, how can they compute, how is communication
established, how is the neural architecture remains stable, how the
brain responds to stimuli and so on. Such questions are very
complicated to solve using a simple spreadsheet package.</P>
<H2 CLASS="western"><A NAME="2.1. INTRODUCTION|outline"></A><FONT FACE="Times New Roman, serif">1.1
NEUROBIOLOGY – THE SCIENCE OF BRAINS</FONT></H2>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Neuroscience includes the analyses of nervous systems to understand
the biological basis of thought and behaviour. It includes the study
of behaviour, the brain, networks of sensory and other neurons, the
neurons themselves, and molecular components of the neurons.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	This field spans today to a wide range of research involving</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Cell physiology and molecular biology of nerve cells. For example
	finding genes encoding for the proteins responsible for nervous
	system function.</P>
</UL>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Biological basis of the normal and abnormal behaviour, emotion and
	response. For example searching for the mental properties by which
	humans interact with others.</P>
</UL>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Bio-informatics principles of connecting neurobiology to computers.
	For example constructing various software and languages to achieve
	full automation.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Describing the development and maintenance of nervous system and
	brain.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Describing the various behavioural responses in different
	environments.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Finding cures for neuro-degenerative and psychiatric diseases
	(Kandel &amp; Squire 2000).</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Communication forms the basis of functioning of nervous systems
which involves the most fundamental signalling unit known as an
Action Potential. An action potential is a change in membrane
potential across an excitable membrane generated by activity of
voltage gated ion channels present in the membrane in an excitable
cell. These voltage gated ion channels are activated by difference in
electric potential across the channels which allow the opening or
closing of ion channels so that ions can enter or leave the cell and
thus cause a series of depolarisation and hyper-polarisation events.
This potential difference across the membrane forms the basis of
communication within a neuron. (Bear<I> et al.</I> 1996)</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	When a neuronal response is invoked by external stimuli, the action
potential comes into play and reaches the synapses of neuron. The
synapse is responsible for passing the message from one neuron to
another. The ion channels open causing calcium ions to flow into
cell, causing the synaptic vesicles to fuse with the cell membrane.
This releases in the contents, known as neurotransmitters, by
exocytosis. These then diffuse through the synaptic cleft. They bind
to the post synaptic membrane of the adjacent neuron, which opens ion
channels and causes depolarization or hyperpolarization of the post
synaptic cell membrane, thus generating the postsynaptic response.
The neurotransmitters are reused by breaking them down with the help
of specific enzymes (such as <I>acetylcholine esterase</I> for
acetylcholine neurotransmitter) which is then re-absorbed by the pre
synaptic neuron and thus the ion channels are closed and connection
breaks (Squire 2004).</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
<BR>
</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">1.2 THE
NEUROPHYSIOLOGY EXPERIMENT</FONT></H2>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	The challenge of understanding nervous system function is addressed
by Neurophysiology. It deals with investigating the function of
neurons, circuits of neurons, and brain systems as opposed to their
structure or biochemical composition. It aims to understand how
behavioural responses to sensory stimuli are calculated using neural
circuits.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-left: 1.27cm; margin-bottom: 0cm; background: #ffffff; line-height: 150%">
Different experimental methods are designed for solving these
problems, such as:</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Intracellular recording using micro-electrodes and patch clamp.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Extra cellular field, single unit, and muscle recording.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Optical recording of calcium transients and membrane potential.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Optical stimulation, sensory stimulation (playing sound, movies,
	touching animal).</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Behavioural observation (limb position, behavioural action such as
	choice, social behaviour).</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	For defining problems and finding their solutions using
neurophysiology, we have taken <I>Schistocerca gregaria </I>also
known as the Desert Locust as test animal.  Almost one-tenth of the
world's human population are affected by this insect for their
livelihood. Locusts have the ability to fly rapidly along great
distances and have 2-5 generations per year. Locusts and Grasshoppers
share the family Acrididae but they are not the same. The difference
lies in the fact that locusts can occur in two life phases:
solitarious (living alone) and gregarious (living in groups), whereas
the grasshoppers do not show this feature (Encyclopædia 2009).</P>
<P CLASS="western" ALIGN=RIGHT STYLE="margin-bottom: 0cm; line-height: 150%">
	<SPAN ID="Frame1" DIR="LTR" STYLE="float: left; width: 7.85cm; height: 6.62cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m23764b55.jpg" NAME="graphics2" ALIGN=BOTTOM WIDTH=296 HEIGHT=172 BORDER=0><I>Figure
	1: Phenotypic difference between Solitarious and Gragarious Locust.</I></P>
	<P STYLE="margin-top: 0.21cm"><I>Source:
	http://en.wikipedia.org/wiki/Locust</I></P>
</SPAN>There are changes in the visual system related to changes in
the lifestyle of locusts. The main function of the eye is to transmit
the visual world information to the brain so that the animal can
respond accordingly. This is done through the bundles of fibres that
make up the optic nerves. In
</P>
<P CLASS="western" ALIGN=RIGHT STYLE="text-indent: 0.21cm; margin-bottom: 0cm; line-height: 150%">
Humans, Ganglion cells, situated in the retina of              the
eye send their axons to the brain in the optic nerves. The lens of
the eye focuses a clear image  of the visual world on the retina
(sheet of neurons and photoreceptors lining the back of eye) These
patterns of light and colour activate the sensory receptors and the
complex information is carried to the brain for processing(Bear<I> et
al.</I> 1996).</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	The locust's eye is different to the human eye in the terms of its
position. Humans have simple eyes whereas locusts have compound eyes.
These consist of thousands of individual photo reception units called
Ommatidia. These are located on convex surface and each channels
light to eight radially arranged retinal cells or photoreceptors to
make an image. Visual information is thus processed in thousands of
separate, parallel channels throughout the optic lobe. Locusts can
see forward, backward, and sideways (Christensen 2005).</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	When an animal sees an approaching object, it can avoid collision by
reacting to the object, either when it is some distance away or it
can react at a given time to avoid the collision by monitoring the
expansion of the image projected on the retina by the approaching
object (Gabbiani<I> et al.</I> 1999).This forms the basis of our
experiment.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Visual systems are mostly tuned to the signal features of the
natural environment specific to every animal's own lifestyle. In
birds, collision sensitive neurons signal an approaching object (Sun
and Frost 1998), and in toad tectum, some neurons respond to objects
that look like worms (Ewart 1997). Visual tuning also changes over
time for some species such as in dragonflies when aquatic larvae
develop to flying adults. In polyphenic locusts (arising of different
phenotypes from the same genotype) visual interneurons are re-tuned
in those animals which undergo a significant transformation in their
life style that includes some changes in behaviour and visual input
(Matheson<I> et al.</I> 2004).</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Experimentation in the lab has been done on both types of locusts
(<I>Schistocerca gregaria </I>Forskal) male and female gregarious and
solitarious locusts. LGMD (Lobula Giant Motion Detector) is a
wide-field, motion-sensitive neuron in the locust's visual system
that most strongly responds to objects that approach animals on a
collision course. The activity of LGMD can be measured by measuring
the activity of its post synaptic target neuron DCMD (Descending
Contralateral Movement Detector) which is present just behind it and
they produce a rapid train of spikes.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	<SPAN ID="Frame2" DIR="LTR" STYLE="float: left; width: 16.13cm; height: 14.24cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m751b284b.png" NAME="graphics3" ALIGN=BOTTOM WIDTH=609 HEIGHT=382 BORDER=0><I>Figure
	2: Locust with its central nervous system (top-right) consisting of
	brain and series of ganglia with nerves between them. The recording
	is done for the DCMD nerve using a pair of silver hook electrodes
	wrapped around the connectives in the locust's neck. Bottom-Left is
	a visual stimulus, which is an approaching black box that appears
	onto a collision course, and the electrical response is recorded via
	hook electrodes from several distinct neurons, where DCMD has the
	largest amplitude. Apparent distance and observed angle formed on
	the retina by visual stimulus are the two calculated parameters of
	visual stimulus for observation. (Nielsen</I><SPAN STYLE="font-style: normal">
	et al.</SPAN><I> 2009)</I></P>
</SPAN>The web interface developed in this project was tested on data
generated by the experiments which involved invoking response from
each animal by providing an external stimulus which can be touching a
body part (physical stimuli), playing some noise (auditory stimuli)
or making some object approach to the locust eye as f it is going to
hit it (visual stimuli). All these stimuli invoke neuronal responses
in locust as opening/closing of ion channels which cause the
formation of action potentials. The signals are carried to the brain
and other parts of the nervous system, thus generating the response
to stimuli. The signals recorded during the experiments monitored the
stimuli being presented and the trains of action potentials passing
from the brain to the rest of the nervous system in DCMD.
</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">1.3
DEVELOPMENT OF A LANGUAGE FOR DEFINING EXPERIMENTS</FONT></H2>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Automation is a very important aspect of fast and efficient
experimentation. Automation can in this case be achieved by use of
information technology with mathematical logic and algorithms for
complete result driven experimentation which are efficient and
reliable. It replaces human involvement with computer control. An
experiment involving repeatable steps can be more error prone if a
human being is employed as no two actions of humans can be exactly
similar. In contrast, a computer can generate a similar action for
any number of times as defined by user. Automation can result in
running of an experiment for a long duration without error and more
efficiency which is difficult to achieve without it.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	There are different ways of doing an experiment. This poses some
constraints on developing an ideal algorithm for achieving automation
of those experiments without introducing much variability and reduced
complexity as they different modalities. One solution to this problem
is developing a formal programming language which:</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Defines an experiment so that it can be repeated many times without
	increasing variability.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Defines an experiment with such clarity, such that it can be carried
	out by another user without any communication difficulty.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Allows both simulation and real experiments.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Is structured and defines clear experimental descriptions.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Allows data acquisition and remote accessibility.</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Less variability and high efficiency can be achieved by this kind of
language design which also saves time and work as compared to manual
experimentation.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	The <I>Haskell</I> programming language suits these goals as it is
highly effective tool for this type of exploratory design, the result
of which was the development of <I>Braincurry</I> language (Nielsen<I>
et al.</I> 2009). Haskell is a functional programming language, which
is so called as the programs in that entirely consists of functions.
They receive the argument as a program's input and the result is
generated as the program's output<FONT SIZE=2>. </FONT>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	A functional programming language is fundamental style of computer
programming which treats the computation as evaluation of
mathematical functions and avoids <I>mutable states</I> i.e.
variables do not change their values. Functional programming
emphasises the evaluation and compositions of functions as a means of
computation. Haskell is purely functional and involves type checking
at compile time rather than run time, which is known as <I>static
typing</I>. Purely functional programming has no side effects as the
value of an expression cannot be changed and it can be evaluated any
time. (Hudak 2000) This leads to <I>referential transparency</I>
where one can freely replace the expressions by their values and vice
versa. Referential transparency makes it much easier to reason about
code and formally proves that programs obey certain properties.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	Haskell has <I>higher order functions </I>where, functions take
other functions as parameters and return functions as return values.
This is not possible in imperative style of programming. They are
powerful way of solving programs. (Lipovača 2009). Haskell also
allows <I>higher order types,</I> which are type constructors that
can be filled in with simple types such as integer, character or a
string. They take type as an argument and return a type as result
(Hudak 2000). An array is a well known example. We cannot have values
that have type array but only array of integer etc. is possible. In
imperative programming, a set of instructions are required to be
specified in an algorithmic way to achieve a certain goal whereas in
declarative style, the goal is defined but the way of doing it is not
defined. Declarative programming was chosen over imperative design
for the Braincurry language because of its easy readability. The
order of execution of code gets very less importance in functional
style of programming which allows developing any set of code any time
and anywhere, as code dependence is not given importance. These
benefits make it more worthwhile for using it over imperative
programming.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<SPAN ID="Frame3" DIR="LTR" STYLE="float: left; width: 7.62cm; height: 7.22cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m543401ef.png" NAME="graphics4" ALIGN=BOTTOM WIDTH=276 HEIGHT=186 BORDER=0>
	<I>Figure 3: Programming Taxonomy</I></P>
	<P STYLE="margin-top: 0.21cm"><I>Source:
	<FONT COLOR="#000080"><U><A HREF="http://successfulsoftware.net/"><FONT FACE="Andale Mono, Times New Roman">http://successfulsoftware.net</FONT></A></U></FONT></I></P>
</SPAN>The Braincurry language (Nielsen<I> et al.</I> 2009) was the
first effort to define experiments by a language, and has three
goals:
</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Allowing experiments and data analysis to be described in a way that
	is sufficiently abstract to serve as a definition.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	To facilitate carrying out experiments by executing such
	descriptions</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	To be directly usable by the end users (Nielsen<I> et al.</I> 2009).</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	This allowed scientists to repeat experiments without much
variability in a controlled manner and to test hypotheses. The
Braincurry language supports data acquisition (hardware recording
from the neural tissue) along with computational models and visual
simulation. Haskell supports experimental language design with much
ease and the cycle of assessing and implementing new language
features has been shortened because of the usability of resulting
language. The limited scope of Braincurry language led to the
development of a further high level design the BugPan language which
serves as a descriptive specification of the parts of experiment.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	BugPan is a language currently being developed based on Functional
Reactive Programming (Nilsson<I> et al.</I> 2002). Functional
reactive programming is programming with signals and events as first
class entities (entities which can be assigned to a variable or
passed as a parameter or returned from a function). A signal is a
higher order type. For any type ‘a’, signal of ‘a’ is a
function from time t to a value in ‘a’.  Anything that changes
continuously with time can be captured as a signal. Examples are
position of a computer mouse or in neuroscience, membrane potential,
synaptic conductance, ion concentration, joint angle etc. An event is
a list of discrete occurrences, each having a value in type 'a' and a
time point. Examples are pressing of a key, a mouse click and in
neuroscience, a spike, collision, synaptic release of
neurotransmitter etc. A Duration is a list of temporal extents; i.e.
each having a value in type 'a' along with a start and end time.
Examples are holding a key for certain amount of time, concentration
of drug present in animal during an experiment, etc.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	An experiment in BugPan is defined as a wiring between signals and
events and is denoted as a session which in our lab is being
conducted on a locust. Every new session means a new experiment with
a new animal. A BugPan query is an expression evaluated in context in
which the values representing observations (signals, events and
durations) are in scope. These values get generated whenever an
experiment is run and can be enquired by <I>'bugsess</I>' which is
the query processor for the BugPan. It shows a list of sessions which
are experiments; asks information from a specific experiment and
tells about signals, durations and events defined for an experiment.
These three entities are widely used in functional reactive
programming languages to define a problem.</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">1.4 AIM OF
THE Project</FONT></H2>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
        BugPan is currently being used by Dr.Nielsen for data
acquisition and running of experiments where full automation is
achieved for neurophysiology experiments on locust. Braincurry and
BugPan are under development for describing and analysing experiments
in neuroscience. Although experiments are being done and results are
being generated on a daily basis, the new challenge is to develop a
query language interface for BugPan which interacts with machines of
experiment along with computer system running BugPan language as well
as user for data analysis.</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">1.5 Questions
Developing BugPan Interface</FONT></H2>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	When developing the BugPan interface, we asked the following
questions:</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	What if a user can analyse data directly from the experimental setup
	avoiding any copy errors?</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	What if a user can run experiments and analyse data, directly from
	the sheet, anywhere around the world?</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	What if a user wants to show his experiment and results to someone
	simultaneously?</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	What if someone else has to run the same experiment on user's
	behalf? 
	</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	We kept all these things in mind and developed the BugPan Interface
which is a structured spreadsheet for neurophysiology experiments.
BugPan Interface is being designed for analysis of large datasets,
where each row of it represents a session, and the columns represents
the properties or calculations on each recording and gives results in
a new cell for every respective experiment, which can be analysed by
the user. The user can perform calculations, store the data for later
use and can compare. Data get generated directly from the
experimental setup. This interface is currently modified for analysis
of data being generated by the neurophysiology experiments on locusts
to demonstrate its efficacy and ease of use.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
	BugPan Interface is a graphical user interface (GUI) for BugPan
which is a command line interface (CLI). GUI’s allows users to
interact with a program in a more friendly way than CLI’s. Every
GUI runs a respective CLI. There are merits and demerits for both of
them;</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; background: #ffffff; line-height: 150%">
<BR>
</P>
<TABLE WIDTH=658 BORDER=1 BORDERCOLOR="#000000" CELLPADDING=7 CELLSPACING=0>
	<COL WIDTH=204>
	<COL WIDTH=205>
	<COL WIDTH=205>
	<TR VALIGN=TOP>
		<TD WIDTH=204>
			<P STYLE="margin-top: 0.21cm"><I><B>Virtue</B></I></P>
		</TD>
		<TD WIDTH=205>
			<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><I><B>Graphical user
			interface</B></I></P>
		</TD>
		<TD WIDTH=205>
			<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><I><B>Command line
			interface</B></I></P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=204 HEIGHT=28>
			<P CLASS="western" ALIGN=JUSTIFY><B>1) Ease of use</B></P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>Navigation is easier.</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>Navigation is difficult with
			keyboard.</P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=204>
			<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm"><B>2)
			File System Control</B></P>
			<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><BR>
			</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>Easy file system control, but
			less extensive.</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>Extensive system control. Single
			line commands executing tasks.</P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=204>
			<P CLASS="western" ALIGN=JUSTIFY><B>3) Speed</B></P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm">Better
			for file browsing.</P>
			<P CLASS="western" ALIGN=JUSTIFY><BR>
			</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>Better for system tasks.</P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=204>
			<P CLASS="western" STYLE="margin-bottom: 0cm"><B>4) Resource
			consumption</B></P>
			<P ALIGN=CENTER STYLE="margin-top: 0.21cm"><BR>
			</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>It involves more resource
			consumption as loading of icons, graphics, and messages.</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>It consumes very low resources
			and thus works fast.</P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=204>
			<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm"><B>5)
			Programming</B></P>
			<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><BR>
			</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>Programming can be achieved but
			is less extensive.</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>Best defined for programming.</P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=204>
			<P CLASS="western" STYLE="margin-bottom: 0cm"><B>6) Remote access</B></P>
			<P ALIGN=CENTER STYLE="margin-top: 0.21cm"><BR>
			</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY>It loses scope for remote access
			and working over network thus requires special tools such for X
			server such as putty, ssh etc.</P>
		</TD>
		<TD WIDTH=205>
			<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm">CLI
			allows the remote access and troubleshooting efficiently.</P>
			<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><BR>
			</P>
		</TD>
	</TR>
</TABLE>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><I>Table 1.Contrast
between Graphical User Interface and Command Line Interface.</I></P>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm; border: 1px solid #000000; padding: 0.04cm 0.14cm; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_45ecb17b.png" NAME="graphics5" ALIGN=BOTTOM WIDTH=322 HEIGHT=131 BORDER=0><IMG SRC="TheBugPanInterfacet_html_m84376f2.png" NAME="graphics6" ALIGN=BOTTOM WIDTH=311 HEIGHT=132 BORDER=0></P>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm; border: 1px solid #000000; padding: 0.04cm 0.14cm">
<I>Figure4. A diagrammatic representation of the differences between
Command Line (Ubuntu Terminal) and Graphical User Interface (Ubuntu
Nautilus).</I></P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
A Graphical user interface is more advantageous for new users, who do
not have knowledge of underlying software but the main disadvantage
is that a user can work on the pre-defined options only. What if the
user needs to add some new feature to the software? New need can only
be addressed by modifying the underlying pre-written software which
involves the direct editing of configuration files. So, there was a
requirement for a Graphical user interface to BugPan language so that
new user can flexibly run the experiment without any programming
knowledge complication. 
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">1.6 WHY USE a
WEB INTERFACE?</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	A
synthesis of these two models of Human Computer Interaction can be
formed so that a web interface is the best of both worlds, CLI and
GUI. It could be programmable at the client side. For instance, the
interaction with a server can be scripted with a HTTP client library.
It could be easy to use and understand both by scientists and
programmers. It could use low resources on the server as the graphics
are generated at the client side, which can be turned off by the
user. Also, it could allow easy remote access.</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">1.7 Statement
of the problem</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	The
current research is about adding a new milestone to the era of
experimentation by improving data analysis. The following questions
would like to be answered by this research:</P>
<OL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	Is developing a structured spreadsheet as a web interface possible?</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	It is helpful in analysing data and what aspects are useful?</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	How can it be made efficient?</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	How can this research be applied to other areas, and what is its
	future scope?</P>
</OL>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	The
research will be focussed but not limited to the questions above. 
</P>
<H1 CLASS="western" STYLE="page-break-before: always"><FONT FACE="Times New Roman, serif">2.
METHODOLOGY</FONT></H1>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">2.1 BugPan
Interface System Architecture (GUI)</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%"><B>	</B>The
BugPan Interface is currently designed to be a data analysis
interface for neurophysiology experiments which are being done on
locusts. It includes code for processing user queries. Haskell has
appropriate support for data types and structures where lists are
pre-defined and pervasive (storage is allocated automatically). The
BugPan Interface is designed in different languages. The user web
interface is written in HTML and CSS. It uses JAVASCRIPT for client
side programming and mathematical functions, and PERL is used for
server side programming along with PERL's common gateway interface
library CGI.pm. Asynchronous JavaScript and XML (AJAX) made a
significant contribution to every part of this interface and works in
data retrieval (fetching results in cell), data analysis (raw output)
and data visualisation (generation of graphs) without reloading the
page, which was quite a challenge.</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%"><BR>
</P>
<H2 CLASS="western"><A NAME="3.2. METHODOLOGY|outline"></A><FONT FACE="Times New Roman, serif">2.2
BugPan System Architecture (CLI)</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	‘<I>bugsess’</I>
is the query processor for BugPan language and when typed in terminal
(CLI), it outputs four options which are Haskell functions:</P>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	list: lists the current sessions/experiments present in the system.</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	ask: allows the user to ask a query from a specific session.</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	show: lists observed values in a session. 
	</P>
</UL>
<P CLASS="western" STYLE="margin-left: 1.27cm; margin-bottom: 0cm; line-height: 150%">
Examples of queries for a particular session that can be enquired by
'<I>bugsess'</I> include 
</P>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>ecVoltage :: Signal Real</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>realEvt :: Event Real</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>tStop :: Event ()</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>tStart :: Event ()</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>displacedLoom :: Duration ()</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>program :: Duration String</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>moduleName :: Duration String</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>approachLoV :: Duration Real</I></P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<I>displacedAngle :: Duration Real</I></P>
</UL>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">There
can be any number of queries that can be already defined or tailor
made.</P>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	filter: it filters out the positive sessions for a specific query.</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	So, the motive for this project was to develop a web GUI for BugPan
where results should be outputted using AJAX (without reloading the
page). 
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
For the successful completion of BugPan Interface, a number of things
contributed which include several programming platforms and
libraries.	</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">2.3
Programming Platforms</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%"><FONT SIZE=4><B>	</B></FONT>Technologies
such as Mark up Language (HTML), Client Side Scripting Language
(JAVASCRIPT), presentation language (Cascading Style Sheets) and
Document Object Model (DOM) were all used. DOM allows a way to
interact with contents of the page such as used variables. By
combining a client side scripting language with html, the pages are
actually activated and they become functional so that the user can
perform calculations, create graphs, and carry out other dynamic
actions. (Sanchez-Clark 2007). The languages specifically used are:</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>2.3.1
HTML (Hyper Text Mark up Language)</FONT></FONT></H3>
<P CLASS="western" STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
HTML is a mark up language developed by Tim Berners Lee in 1980,
which forms the basis of creating structured documents on the web by
denoting structured semantics which include headings, lists, tables
etc. It allows the embedding of objects such as images, flash files
and videos to create highly interactive web designs (Sanchez-Clark
2007).</P>
<H3 CLASS="western"><A NAME="3.3.2.3 Programming Platforms|outline"></A>
<FONT FACE="Times New Roman, serif"><FONT SIZE=3>2.3.2 CSS (Cascading
Style Sheets)</FONT></FONT></H3>
<P CLASS="western" STYLE="text-indent: 0.64cm; margin-bottom: 0cm; line-height: 150%">
CSS is a presentation language allowing different interactive
presentations for the content. In CSS, styles can be developed that
control the appearance of content as shown in Figure 5. Once a style
sheet containing formatting options is made, it can be applied to any
of the content and one change in that will be reflected in the
appearance of whole sheet (Meyer 2006).</P>
<P CLASS="western" STYLE="margin-left: 1.27cm; margin-bottom: 0cm; line-height: 150%">
<SPAN ID="Frame4" DIR="LTR" STYLE="float: left; width: 15.75cm; height: 7.09cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m4ae06a1f.jpg" NAME="graphics7" ALIGN=BOTTOM WIDTH=595 HEIGHT=201 BORDER=0><I>Figure
	5: Left, HTML table with applied CSS formatting. Right, same table
	without CSS formatting. Source: BugPan Interface
	(http://bioinf3.bioc.le.ac.uk/~ss533/CGI-bin/sheet.CGI)</I></P>
</SPAN><BR>
</P>
<P CLASS="western" STYLE="margin-left: 1.27cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 1.27cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 1.27cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>2.3.3
JAVASCRIPT (Client Side Scripting Language)</FONT></FONT></H3>
<P CLASS="western" STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
JavaScript is a client side scripting language that allows
programmatic access to the objects, so it is also known as an object
oriented scripting language. It allows development of advanced user
interfaces and interactive dynamic websites. It allows validation and
other actions to be performed without sending the page back to the
server. This lightweight programming language is an interpreted
language, which means the scripts execute themselves without
preliminary compilation and furthermore there is no licensing
required for its use (Flanagan &amp; Ferguson 1998).</P>
<P CLASS="western" STYLE="margin-left: 1.27cm; margin-bottom: 0cm; line-height: 150%">
<B>	</B></P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>2.3.4
AJAX (Asynchronous JavaScript and XML) </FONT></FONT>
</H3>
<P CLASS="western" STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
AJAX is a very important component of the BugPan Interface. It allows
retrieving data from the server asynchronously in the background
without affecting the visual response on the browser. The data is
retrieved using XMLHttpRequest Object. XMLHttpRequest allows the
sending of HTTP or HTTPS requests directly to the server and then
loading back the server response directly to the scripting language.
Before the advent of Ajax, websites were indulged in submit-wait
paradigm that increases response time, and actions such as
text-typing or drawing with prompt responses could not be expected as
they had to wait for the server reply. This has been removed by use
of Ajax.</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">Merits
of using Ajax other that its fast request handling property are:</P>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	The bandwidth usage can be reduced as only requested content is
	reloaded not the whole page.</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	It reduces connections to the server, since scripts have to be
	requested only once.</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	A state can be maintained throughout the website, with non changing
	values of JavaScript variables (Johnson et al. 2007).</P>
</UL>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	We
made use of JavaScript libraries which ease scripting complications
and allow crossbrowser facilities viz., Prototype, Scriptaculous,
Light Box, and Fish Eye Menu. Prototype is a JavaScript framework
having a number of features which makes working with AJAX very easy.
It hides the complexity from the user and provides a hierarchy of
Ajax helper objects, using its own object inheritance system. These
helper objects are provided with generic base classes being sub
classed by more of the focused helpers that allows the coding of most
of them in a single line. Scriptaculous is a JavaScript library which
delivers a rich set of high level functionality by providing high end
visual effects such as drag and drop, show-hide of objects on page
using Prototype. (Crane et al. 2007)</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>2.3.5
PERL (Server Side Scripting Language) </FONT></FONT>
</H3>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	PERL
is a high-level dynamic programming language developed by Larry Wall
in 1987 and stands for Practical Extraction and Report Language. It
has powerful text processing facilities, along with system
administration, networking, database access, graphics programming,
and CGI web programming. It includes support for multiple programming
paradigms (object-oriented, functional, and procedural), text
processing built-in support, and a large collection of third party
modules such as CGI.pm etc. It allows easy file handling, pattern
match, integration with JavaScript functions, and functionality
across networks all of which makes it more supportive and extensive
to use (Liang 2004).</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>2.3.6
CGI (Common Gateway Interface)</FONT></FONT></H3>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	CGI
is defined as a protocol (a set of calling rules) for interfacing
external application software with an information server. A server is
a program delivering services to clients. The server and the client
programs can run on same or different computers over the network. We
made use of the CGI.pm module, which is a stable solution for the
processing and preparing of HTTP responses. It includes form
validation and submission, reading and writing cookies, file uploads,
generation of query strings and manipulation. It can be programmed as
object-oriented and as function oriented style. We used the object
oriented style for designing the BugPan Interface (Stein 1998).</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">2.4 Servers
used</FONT></H2>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>thttpd</B> – It is called as tiny/turbo/throttling HTTP server.
	This is a fast, portable and secure http server. We installed it as
	a local server for daily editing and manipulation of scripts.</P>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>Apache</B> – Apache HTTP server is a web server which is widely
	used all around the world and plays an important role in the growth
	of the World Wide Web. It runs more than 100 million websites.
	Apache is very powerful and allows more security and options for the
	websites. We used it on University's web server for hosting of
	BugPan Interface.</P>
</UL>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">2.5 Editors
useD</FONT></H2>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>gedit – </B>A lightweight editing tool which supports plugins
	and other useful options.</P>
</UL>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">2.6 Debuggers
used</FONT></H2>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>Firebug</B> – Firebug is a very powerful tool and allows
	editing, debugging of all HTML, CSS, JavaScript scripts and gets
	integrated with Firefox.</P>
</UL>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">2.7
Statistical Software used</FONT></H2>
<UL>
	<LI><P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>R</B> – A language platform for statistical computing and
	graphics developed at Bell labs.</P>
</UL>
<H1 CLASS="western" STYLE="page-break-before: always"><A NAME="4.3 RESULTS|outline"></A>
<FONT FACE="Times New Roman, serif">3 </FONT><FONT FACE="Times New Roman, serif">RESULTS</FONT></H1>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">3.1
DEVELOPMENT OF THE BUGPAN INTERFACE</FONT></H2>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	The development of an interface for the BugPan language started with
the motive of making a platform for neuroscientists, where they can
start their own experiment, generate data, analyse it and then save
and retrieve results globally while working on a web-browser. Running
new experiments and data analysis of previous ones was given a new
direction by the BugPan language but the major thing lacking was a
web interface where:</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	All the experiment sessions can be visualized on a single platform,</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Individual queries can be run on them, 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	The data can be analysed on the web browser, 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Graphs can be produced of the data generated which helps the easy
	characterization of data,</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Calculating statistics such as 'mean' and 'standard deviation', 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Running multiple queries on single session and comparing data for
	the same or different sessions for the same or different queries,</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Saving the sheet and reverting it back later, 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Saving the sheet in .xls format so as to be compatible with a
	spreadsheet package for further analysis.</P>
</UL>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	The aim was to achieve all of the above without the end user
requiring extensive knowledge about any programming language and just
with the help of few clicks. It was quite a challenge to make a web
GUI for a language which runs on the command line, and the GUI should
be accessible from any part of the world. The challenge was accepted
and the development of BugPan Interface started.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
Initial tools picked were HTML, PERL &amp; CGI and this list extended
to JavaScript, Ajax, CSS, and R as project progressed.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">3.2 BUGPAN
INTERFACE FRAMEWORK</FONT></H2>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>3.2.1
THE BUGPAN INTERFACE SHEET</FONT></FONT></H3>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
The most vital and central part of the BugPan web interface is the
spreadsheet. The BugPan spreadsheet is a grid where by default; the
number of rows depends on the number of sessions known to ‘<I>bugsess</I>’
and the number of columns is fixed, but can be increased by adding.
The first column shows the Session Names which are unique hexadecimal
numbers generated by BugPan. For the sake of simplicity, only first
six characters are shown. The next column is Start Time, and tells
about the date when the particular session was created. The third
column shows the Module Names, which are BugPan experiment
definitions that tells which session runs which modules. Currently,
the programs in BugPan that define the experiment are:</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>displacedLoom</B>– this module runs a real time experiment and
	is looming object generation for collision course on a random angle,
	with all the experimental setup in place.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>Intfire</B>–this module provides an integrate and fire
	simulation of synaptic input into a neuron.</P>
</UL>
<H3 CLASS="western" ALIGN=RIGHT><FONT FACE="Times New Roman, serif"><FONT SIZE=3>T<SPAN ID="Frame5" DIR="LTR" STYLE="float: left; width: 6.99cm; height: 7.2cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m4e53e173.jpg" NAME="graphics8" ALIGN=BOTTOM WIDTH=262 HEIGHT=171 BORDER=0><I>Figure
	6: Lists all the sessions/experiments along with Start time and
	Modules run on that experiment, without executing any query.</I></P>
</SPAN>HE </FONT></FONT><FONT FACE="Times New Roman, serif"><FONT SIZE=3>BUGPAN
INTERFACE GRID</FONT></FONT>
</H3>
<P CLASS="western" ALIGN=RIGHT STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
	This default table (Figure 6) gets generated when the sheet is
opened. It fetches the session (experiment)</P>
<P CLASS="western" ALIGN=RIGHT STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
names which are folders in the file system defined by BugPan. Every
folder is an experiment and contains 
</P>
<P CLASS="western" ALIGN=RIGHT STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
data stored as lists which can be enquired by queries. 
</P>
<P CLASS="western" ALIGN=RIGHT STYLE="margin-left: 0.64cm; margin-bottom: 0cm; line-height: 150%">
The session list is generated for sessions present in the system.
When a module is made to run once, a set of values are being
generated which we call as data. The motive of BugPan the interface
is to analyse this data. The number in the round parenthesis
following the module name tells how many times the specific module
has been run for a specific session. Generating of sessions in form
of table rows, ease their enquiry.</P>
<H3 CLASS="western"><A NAME="4.2.3.2 BUGPAN INTERFACE FRAMEWORK|outline"></A>
<FONT FACE="Times New Roman, serif"><FONT SIZE=3>3<SPAN ID="Frame6" DIR="LTR" STYLE="float: left; width: 9.79cm; height: 8.93cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m564390b8.png" NAME="graphics9" ALIGN=BOTTOM WIDTH=369 HEIGHT=219 BORDER=0><I>Figure7:
	A query is executed by adding new query column; first three
	experiments return empty values for that query where as the fourth
	one is showing graph. When migrated to that cell via keyboard, it
	displays more information about that session value using Ajax below
	spreadsheet.</I></P>
</SPAN>.2.2 SHEET FUNCTIONS</FONT></FONT>
</H3>
<H4 CLASS="western">3.2.2.1 ASKING QUERY (ADD QUERY COLUMN)</H4>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">After
generating a table with the experiment’s name, the query can be
asked. For that '<I>add query column' </I>option was defined. It adds
a new column with same number of rows that are already present as
shown in</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">Figure7.
A space is added for every session where the output of query will be
displayed. The top cell defined as ‘ask query’ cell enables the
query to be entered. The output can take any form depending on the
query and the data stored, and is presented in the newly defined
column of output cells.</P>
<TABLE WIDTH=658 BORDER=1 BORDERCOLOR="#000000" CELLPADDING=7 CELLSPACING=0>
	<COL WIDTH=72>
	<COL WIDTH=48>
	<COL WIDTH=71>
	<COL WIDTH=73>
	<COL WIDTH=72>
	<COL WIDTH=75>
	<COL WIDTH=59>
	<COL WIDTH=74>
	<TR VALIGN=TOP>
		<TD WIDTH=72>
			<P CLASS="western"><B>Value count</B></P>
		</TD>
		<TD COLSPAN=7 WIDTH=556>
			<P CLASS="western" ALIGN=CENTER><B>DATA TYPES</B></P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=72>
			<P CLASS="western">Result value count</P>
		</TD>
		<TD WIDTH=48>
			<P CLASS="western" STYLE="margin-bottom: 0cm">Empty</P>
			<P CLASS="western">Data</P>
		</TD>
		<TD WIDTH=71>
			<P CLASS="western">Empty Event</P>
		</TD>
		<TD WIDTH=73>
			<P CLASS="western">Event Real</P>
		</TD>
		<TD WIDTH=72>
			<P CLASS="western">Duration ()</P>
		</TD>
		<TD WIDTH=75>
			<P CLASS="western">Duration Real</P>
		</TD>
		<TD WIDTH=59>
			<P CLASS="western">Duration String</P>
		</TD>
		<TD WIDTH=74>
			<P CLASS="western">Signal</P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=72 HEIGHT=53>
			<P CLASS="western">One</P>
		</TD>
		<TD WIDTH=48>
			<P CLASS="western">[]</P>
		</TD>
		<TD WIDTH=71>
			<P CLASS="western" STYLE="margin-bottom: 0cm">Real Number</P>
			<P CLASS="western">(Start Times)</P>
		</TD>
		<TD WIDTH=73>
			<P CLASS="western" STYLE="margin-bottom: 0cm">Real Number</P>
			<P CLASS="western">(associated value)</P>
		</TD>
		<TD WIDTH=72>
			<P CLASS="western" STYLE="margin-bottom: 0cm">Real Number</P>
			<P CLASS="western">(start time, end time)</P>
		</TD>
		<TD WIDTH=75>
			<P CLASS="western" STYLE="margin-bottom: 0cm">Real Number</P>
			<P CLASS="western">(associated value)</P>
		</TD>
		<TD WIDTH=59>
			<P CLASS="western">String</P>
		</TD>
		<TD WIDTH=74>
			<P CLASS="western">Histogram</P>
		</TD>
	</TR>
	<TR VALIGN=TOP>
		<TD WIDTH=72>
			<P CLASS="western">More</P>
		</TD>
		<TD WIDTH=48>
			<P CLASS="western">[]</P>
		</TD>
		<TD WIDTH=71>
			<P CLASS="western">Histogram</P>
		</TD>
		<TD WIDTH=73>
			<P CLASS="western">Histogram</P>
		</TD>
		<TD WIDTH=72>
			<P CLASS="western">Histogram</P>
		</TD>
		<TD WIDTH=75>
			<P CLASS="western">Histogram</P>
		</TD>
		<TD WIDTH=59>
			<P CLASS="western">String</P>
		</TD>
		<TD WIDTH=74>
			<P CLASS="western" STYLE="page-break-after: avoid">Series of
			Histograms</P>
		</TD>
	</TR>
</TABLE>
<P STYLE="margin-top: 0.21cm"><I>Table 2 Table representing different
output possibilities for different data types and value counts.</I></P>
<H4 CLASS="western">3.2.2.2 Annotating Sessions (ADD USER COLUMN)</H4>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">
Data annotation is implemented in the BugPan Interface and is a
powerful tool allowing a user to add new values to a particular
session or all of them. The option defined to user is <I>'add user
column'. </I>On clicking, this button, a new column is added to the
top cell, displaying USERCOLUMN. The value of the top cell should be
replaced by the value or string name to be added into the session
data list, and the cells following that will contain the numeral
values which the user needs to store in the sessions as shown in
Figure 10. The value is of type Duration Real. The value added can be
enquired later by asking it as query from query column and the stored
values will appear in the cells following it.</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; border: 1px solid #000000; padding: 0.04cm 0.14cm; line-height: 150%; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_2d08d505.png" NAME="graphics10" ALIGN=BOTTOM WIDTH=642 HEIGHT=225 BORDER=0></P>
<P STYLE="margin-top: 0.21cm; border: 1px solid #000000; padding: 0.04cm 0.14cm">
<I>Figure 8: Figure demonstrating session annotations. Adding’
test’ as a value in user column with the numerical values that are
needed to be added for the corresponding sessions. The same value is
enquired as a query using query column outputting the added values.</I></P>
<H4 CLASS="western">3.2.2.3 FILTERING (QUERY ON SPECIFIC SESSIONS) 
</H4>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	Filtering
is used to sort out required elements from a pool of elements. This
is a very important tool as it allows analysis of only the required
things. It saves time and data iteration in some cases. This tool is
defined in the BugPan interface and allows a user to filter out
sessions for a particular query that return true and false values.
The sessions returning true will be outputted in the form of a new
table and the sessions returning false will be empty lists and will
not be included in the grid. This saves time along with resource
consumption as only specific sessions will be queried which is a
different scenario from querying all sessions which can make analysis
difficult.</P>
<H4 CLASS="western">3.2.2.4 REQUIRE STATISTICS (CALCULATE STATISTICS)</H4>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	Statistics
is used to evaluate results. They can state directly or indirectly
the efficiency of an experiment. They give a summary of the whole
data set such as mean and standard deviation. The BugPan interface
includes a function for the calculation of statistics, including mean
and standard deviation. These functions calculate the statistics for
the data appearing in cells, and outputs in the cell defined for mean
and standard deviation at the bottom rows of the grid. If the values
for sessions are not numeric i.e. in the case of empty values, or
graphs as outputs, the result will be '<I>NaN</I>'.</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>3.2.3
MORE DATA REPRESENTATION</FONT></FONT></H3>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	Another
important part of the BugPan interface is data representation in
graphical, tabular and raw form which is generated by the program.
Data representation in different forms for a query result got its
inspiration from Wolfram Alpha. Wolfram Alpha is a computational
search engine which attempts systematic computational knowledge
calculations for any query (Wolfram Alpha 2009)
(http://www.wolframalpha.com/). It displays the result of a query in
the form of graphs, values, calculated statistics, maps etc. in many
possible ways as appropriate to the data and query. In the BugPan
Interface, the same theme was applied. So, when the user presses a
cell which has some output, generated by a particular query for a
particular session, the BugPan interface displays more and more
information about that data. If it is a single value, then the
interface reports that session selected is 'selected session' for the
entered query and outputs the value in raw format as generated by
<I>'bugsess'</I> on command line. If the cell contains a histogram,
then the output is a list of values, with a link. Clicking on that
runs Ajax to display more and more result representations below the
grid in new division. It involves the graphical representation, with
a number of histograms and scatter plots for different values of
data, clicking on them launches them in new interactive window where
the user can navigate between the graphs and can save them as well.
If the query is enquiring signal, then the graph is a series of plots
else it is a histogram of data values in case of event and duration.
The next division is the tabular representation, where the data
values get broke out in tabular format with a break after every seven
entries to fit into the screen thus presenting clear data. The last
part is the raw output as generated by command line.</P>
<P CLASS="western" ALIGN=CENTER STYLE="margin-bottom: 0cm; line-height: 150%">
<B>G<SPAN ID="Frame7" DIR="LTR" STYLE="float: left; width: 16.82cm; height: 11.04cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m132f4bf4.png" NAME="graphics11" ALIGN=BOTTOM WIDTH=635 HEIGHT=330 BORDER=0><I>Figure
	9: Migrating to specific cell displays information (graphical,
	tabular, raw output) about that cell, where first part is graphs
	which are generated by 'R' statistical software .Middle histogram is
	generated for the associated value of real event (realEvt) which in
	this case is same for every observation making a block in histogram.
	Last is a scatter plot of start &amp; end times.</I></P>
</SPAN>raphical Data Representation for query 'realEvt' and session
'ebcd0a'.</B>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">Clicking
on graph opens that graph on the screen, where the user can migrate
to other graphs.</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; border: 1px solid #000000; padding: 0.04cm 0.14cm; line-height: 150%; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_m66ec6a01.jpg" NAME="graphics12" ALIGN=BOTTOM WIDTH=641 HEIGHT=233 BORDER=0></P>
<P STYLE="margin-top: 0.21cm; border: 1px solid #000000; padding: 0.04cm 0.14cm">
<I>Figure 10 Clicking on graph generates a window pane, where user
can migrate between different graphs and can save them as well. At
the bottom, it displays that which graph the user is currently
viewing and how many graphs there are in total. Migration can be done
via keyboard and mouse.</I></P>
<H2 CLASS="western"><FONT FACE="Times New Roman, serif">3<SPAN ID="Frame8" DIR="LTR" STYLE="float: left; width: 17.02cm; height: 5.55cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m97fbf01.png" NAME="graphics13" ALIGN=BOTTOM WIDTH=634 HEIGHT=165 BORDER=0><I>Figure
	11: Displays the data in tabular form, after the graphical
	representation, which it generates from the raw data which is
	displayed in the last section and named as RAW OUTPUT.</I></P>
</SPAN><BR CLEAR=LEFT>.3 BUGPAN LAYOUT</FONT>
</H2>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
In addition to its spreadsheet, the BugPan Interface has different
areas for navigation and control.</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>3.3.1
BUGPAN MAIN MENU</FONT></FONT></H3>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	This menu displays the header of the BugPan Interface along with the
image of a locust which has a hyperlink to the locust information
resource. The main menu is controlled by Fisheye menu, which
simulates Rocket menu navigation as in Apple's Macintosh's operating
system.</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>3.3.2
BUGPAN FILE MENU</FONT></FONT></H3>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 0.64cm; margin-bottom: 0cm; line-height: 150%">
The BugPan file menu includes the file options which are JavaScript
functions namely:</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="line-height: 150%"><B>Add</B>:
	adds query column.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="line-height: 150%"><B>Add
	User Column</B>: adds a new user column to the existing spreadsheet,
		</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="line-height: 150%"><B>Save
	User File</B>: saves the current user queries in a new user named
	file for later retrieval.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="line-height: 150%"><B>Calculate
	Statistics</B>: calculates the statistics, 'Mean' and 'Standard
	Deviation'. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="line-height: 150%"><B>Save
	as xls</B>: saves the grid contents in .xls file for viewing in
	spreadsheet packages.</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="line-height: 150%"><B>Reset</B>:
	resets the sheet to the start point.</P>
</UL>
<H3 CLASS="western"><A NAME="4.3.3.3 BUGPAN LAYOUT|outline"></A><FONT FACE="Times New Roman, serif"><FONT SIZE=3>3.3.3
BUGPAN SEARCH MENU</FONT></FONT></H3>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
The BugPan Interface has got its own search engine which has been
designed with the courtesy of Google.com. The search engine is
currently restricted to ten important websites, for the search on
biological information. It can be accessed individually by clicking
on BugPan Search Engine link.</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>3.3.4
BUGPAN SHEET MENU</FONT></FONT></H3>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	BugPan File menu allows users to retrieve their saved sheets,
history (navigation) files and the .xls (spreadsheet) files. The
first section displays a live running clock which keeps track of
seconds, so the user can keep track of time. The next section
displays hide/show options for hiding sheet and menus. It includes
reset sheet along with a text box naming filter values, which is used
for session filtering. The last section is file section displaying
user files being classified as User Sheets, History files and xls
files which store the user queries, sheet navigation steps, and grid
contents.</P>
<H3 CLASS="western"><FONT FACE="Times New Roman, serif"><FONT SIZE=3>3.3.5
BUGPAN STATUS NAVIGATOR</FONT></FONT></H3>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%"><B>Sheet
Navigation System (Full Keyboard Control)</B></P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="text-indent: 1.25cm; line-height: 150%">
The Sheet Navigation System used in the BugPan Interface allows a
user to automate and have the full control of the web spreadsheet via
keyboard as we have in spreadsheet packages. If the spreadsheet had
been implemented as a simple html or dynamic table, users would have
needed to migrate between the columns by mouse clicks. Instead this
concept is completely automated and the full spreadsheet migration is
defined by keyboard. Navigation can be activated by pressing the keys
'G' and then 'O' making <I>GO</I>; no other key press can activate
the sheet navigation system. Once the 'GO' is pressed, it asks for
the user name then whether the user wants to save sheet navigation
history that will store with the user specified file name. After the
sheet is activated, the first box or cell of the sheet is highlighted
and this indicates sheet activation. Now the user can migrate to the
right cell by pressing the right '-&gt;' key on the keyboard and same
is being defined for the others viz., 
</P>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	↑ -- UP <B>↓</B> -- DOWN <B>←</B> -- LEFT <B>→</B> -- RIGHT 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>a</B> -- Selects the user query, and allows custom selection for
	more than two columns. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>c</B> -- Calculates the statistics for the result values. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>f</B> -- Takes the user to the filter text box, so that some
	session filtering can be done. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>n</B> -- Makes a new query column so that some user query can be
	commenced. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>r</B> -- Resets the sheet to the start point. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>s</B> -- Prompts the user for the file name and saves the sheet
	with that file name. 
	</P>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	<B>w – </B>Focuses the user query, and allows custom selection for
	more than two columns. 
	</P>
</UL>
<UL>
	<LI><P CLASS="western" ALIGN=JUSTIFY STYLE="line-height: 150%">	The
	sheet navigation status bar displays the full information for the
	current selected cell which runs Ajax (getting results without
	reloading the page). For every keyboard action, the second line of
	the Status for Sheet Navigator gets replaced by the pressed key and
	displays the action associated with it such as <I>commencing user
	query, left, right, up, down, saving sheet </I>etc. All actions done
	in one session by user can be retrieved later at any point of time
	as a text file, if the user saved the history. Blackbird (Olson
	2009) is also being used as a display panel for user navigation
	steps. The sheet can be activated by <I>proto.menu</I> (Zaytsev
	2009) as well which gets activated when the user pointer is over the
	sheet enabling access to sheet file menu options.</P>
</UL>
<H1 CLASS="western"><FONT FACE="Times New Roman, serif">4. DISCUSSION</FONT></H1>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%"><FONT SIZE=4>	The
</FONT>BugPan Interface is a domain-specific language interface for
scientific experimentation and data analysis currently being
developed for a neurophysiology experiments on locusts. The data
generated by these experiments was used as a test-bed for the BugPan
Interface, which has successfully accomplished all goals.</P>
<H2 CLASS="western"><A NAME="5.1.TESTING Hypothesis|outline"></A><FONT FACE="Times New Roman, serif">TESTING
Hypothesis</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
We framed questions as a part of hypothesis testing and at the end of
the research; the answers came out to be positive. Developing a
structured spreadsheet web interface was successfully accomplished in
the form of BugPan Interface. It is very helpful for analysing data
as the data can be represented in many forms, as graphical and
tabular with options for calculating statistics and filtering of
experiments. BugPan Interface is well suited for exploratory data
analysis which involves analysing data for hypothesis formulation and
testing purposes. It assesses assumptions and causes of the observed
phenomena and supports the selection of statistical tools and
techniques. Most useful aspects are the use of Ajax for displaying
information which delivers a richer user-experience and improves the
efficiency of BugPan interface. This technology increases the
responsiveness of applications and has previously been used by
MachiBase (http://machibase.gi.k.u-tokyo.ac.jp/) which is a genome
browser for <I>Drosophila melonagaster</I> (Ahsan et al. 2009).  Use
of Ajax for data analysis in the form of a structured spreadsheet web
interface is a new concept for biological experiments. Developing web
applications in Ajax is a complex task, but the use of JavaScript
libraries kept it manageable as they hide most of the complexity from
the user. Development can be achieved in other platforms as well but
they were far too complex for the scope of this project. Keyboard
navigation was used in the BugPan web interface for spreadsheet
simulation, which delivers high end performance by displaying more
information for the selected cell of the sheet which can not be
achieved in a simple spreadsheet package. The BugPan interface
combines advantages of a spreadsheet with those of operating on-line
software which allows running experiment and data analysis from any
part of the world. Filtering allows positive experiments as outcome
for a certain query and for deep investigation of specific
experiments according to data contained in them. The User column
feature allows annotation of sessions by inserting values manually
for a particular session or all of them.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	ECR Browser (Ovcharenko<I> et al.</I> 2004)
(http://ecrbrowser.dcode.org/) is a tool for accessing and
visualizing data from comparisons of multiple vertebrate genomes. It
is more extensive in scope than the BugPan Interface. It allows
structured analysis, filtering by removing or adding the species. It
is not an actual spreadsheet interface as species are defined in rows
but columns are not defined as results as they have zooming options
in place. It also allows different views of data along with custom
annotation features which are included in the BugPan Interface as
well. Main feature that compares both interfaces is they generate
their own data for analysis.</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; line-height: 150%">	The
spreadsheet aspect of the BugPan Interface using Ajax can be
effectively applied to other areas such as phylogeny analysis where
the different species can be aligned in rows forming the experiments
with sequence in the top cell as query and the output will be the
Basic Local Alignment Search Tool or BLAST (Altschul<I> et al.</I>
1990) (<FONT COLOR="#000080"><A HREF="http://blast.ncbi.nlm.nih.gov/Blast.cgi"><FONT COLOR="#000000"><SPAN STYLE="text-decoration: none">http://blast.ncbi.nlm.nih.gov/Blast.cgi</SPAN></FONT></A></FONT>)
result in every cell for every species. Homology modelling is also
possible with protein super families in the rows for querying with
novel protein sequence as the query and the output will be the
modelled structures by the use of modelling software such as Modeller
(Eswar<I> et al.</I> 2008). Data annotation for novel sequences in
genomes can also be performed using user column doctrine and running
statistical software like '<I>R</I>' (Hornik 2009), '<I>statistica</I>'
(StatSoft 2009) allow achieving sophisticated data analysis for other
scientific experiments as well.</P>
<H2 CLASS="western"><A NAME="5.2.CHALLENGING CURRENT DEVELOPMENTS|outline"></A>
<FONT FACE="Times New Roman, serif">CHALLENGING CURRENT DEVELOPMENTS</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
The BugPan Interface idealizes the data management by a motive of
integrating experimentation which will be added as an extensive
feature to the current BugPan Interface, and analysis on the same
platform which is lacking in existing web interfaces such as Circos
(Krzywinski<I> et al.</I> 2009) (http://mkweb.bcgsc.ca/circos/) or
Mobyle (Neron<I> et al.</I> 2009)
(http://mobyle.pasteur.fr/cgi-bin/portal.py). Circos is an
application which allows data representation in highly interactive
forms for the inputted data. Mobyle is a bioinformatics analysis web
environment which data analysis using number of different software
packages. These interfaces allow different types of data
characterization and representation but they require input from the
user and thus have restrictions on the data format which is solved to
some extent by the BugPan Interface. It keeps hold of the data at the
server which gets generated by running experiments at the interface
and can be queried and the user need not store and upload files
again. This can lead to new generation of software development, which
includes data generation, data management and data analysis in the
same platform, reducing the search for efficient data analysis tools.
Ultrascan is a GUI data analysis package for the hydrodynamic data
from ultra centrifugation experiments. This accepts data files
generated by Beckman data acquisition software but other files need
editing (Brookes<I> et al.</I> 2009). Other problems with existing
interfaces include no remote access, slow processing and a
complication with the usage of different data analysis options. On
comparison basis, data acquisition is included in experiments
implemented by the BugPan language which converts the analogue
signals to digital format and that produces the data. The BugPan
Interface is designed such that it automatically fetches the data,
generates histograms, ‘xy’ plots and produces the data in tabular
and raw output as well, which is sometimes important to know the
output generated by machine. It uses low resources on the server by
storing only the queries but not their results. When opened later the
query is again queried for all experiments which show result update
as well. If a user has to make some additional variables and values
for the experiments, they can be achieved by using the user column.</P>
<P CLASS="western" STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
BugPan allows the analysis to be conducted in a spreadsheet format as
it simulates working on paper grid allowing user interactivity with
experiments in rows and query results in columns. This allows data
analysis in a pleasant way which lacks in IlluminaGUI (Schultze &amp;
 Eggle 2007) (<FONT COLOR="#000080"><A HREF="http://illuminagui.dnsalias.org/"><FONT COLOR="#000000"><SPAN STYLE="text-decoration: none">http://illuminagui.dnsalias.org/</SPAN></FONT></A></FONT>)
and Statistical viewer (Stenger<I> et al.</I> 2005). They lack the
different shape views of data as offered by a spreadsheet design.
IlluminaGUI analyses the data generated by Illumina sequencer thus
integrates data generation and analysis and calculating statistics,
as used in BugPan. However, it lacks web access and a structured
query format. BugPan allows web access which is not observed in GATA
(Nix &amp;  Eisen 2005) (http://gata.sourceforge.net/). GATA is a
graphic alignment tool for comparative sequence analysis but is
provided as a Java application that lacks the remote access
functionality. It restricts the user to a local machine. GenomeGraphs
(Durinck<I> et al.</I> 2009) is add on package for the statistical
programming language R and performs visualization of genomic
datasets. It also plots custom annotation tracks along with different
experimental data types allowing data analysis with graphical
representation. As it is provided an R add on package, it restricts
the user to the local machine. The BugPan Interface also uses R
package known as ‘Cairo’ (Urbanek 2005) for making graphical
representation of data, giving privileges to user to use R software
package online from any where in the world.</P>
<P CLASS="western" STYLE="text-indent: 1.25cm; margin-bottom: 0cm; line-height: 150%">
Developing a web GUI with the use of Ajax makes it efficient. Apart
from technical benefits, it reduces the steps needed to complete the
task and generates a familiar user interface with low training costs
as fewer options are need to be defined and learned because the data
is generated automatically. In many cases output becomes the input
for another output. For instance, fetching a query result in form a
graph and clicking the graph represents data in different formats
without reloading the page and avoiding the submit-wait paradigm
which was observed in AlignPort (Dziubecki &amp; Zola 2006).
AlignPort tries to reduce the submission-retrieval cycle but can not
match Ajax technology speed for sending and receiving of requests. It
also improves the application responsiveness as users can migrate
from one result to another and they can visualize the work flow which
is a very different situation in the case of less responsive
applications involving inputting data, waiting, downloading and
uploading files for another task which makes the user eccentric and
balky. So, BugPan Interface tries to fill the loop holes of different
software packages to provide a complete solution to the problem of
data analysis.</P>
<H2 CLASS="western"><A NAME="5.3.FUTURE SCOPE|outline"></A><FONT FACE="Times New Roman, serif">FUTURE
SCOPE</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	The future scope of the spreadsheet is to be a fully fledged
platform for data analysis of scientific experimentation which can be
designed at interface with defined parameters by the user. A complete
secure login system will be defined for data protection for academic
and commercial purposes. Data analysis will include the literature
and other resources linked with the specific experiment. There is a
scope for producing graphical presentations of highly sophisticated
models of complex biological systems as provided by UCSC genome
browser (Mangan<I> et al.</I> 2009) (http://genome.ucsc.edu/). Each
biological system such as Nervous or Skeletal system can be queried
for a specific gene or protein sequence and id, a map along with
detailed phylogeny analysis for different genes and homology
modelling for the different protein sequences which can take form of
structures spreadsheet. More data analysis options such as t-tests,
analysis of variance, and regression analysis can be added along with
multiple spreadsheet views for extensive data analysis. There is a
scope for including professional blog and communication systems for
scientists as well as a visual simulation for real experimental setup
with animal response.</P>
<H1 CLASS="western"></H1>
<H1 CLASS="western" STYLE="page-break-before: always"><FONT FACE="Times New Roman, serif">5.
CONCLUSION</FONT></H1>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	The BugPan interface is a new generation web interface, which allows
the experiment handling, data analysis to be carried out in a way
where user has advantages of spreadsheet packages as well as web
access for data analysis of experiment data in graphical and tabular
form. This leads to a single platform for defining experiments, and
handling data in a more organised way using new generation web
technologies such as Ajax. Applying Ajax to biological experiment
data analysis in the form of structured spreadsheet with the
advantage of starting new experiments from an interface forms a
complete new area of research with currently no significant
publications. This could mark a breakthrough in the world of data
management.</P>
<H1 CLASS="western" STYLE="page-break-before: always"><FONT FACE="Times New Roman, serif">6.
ACKNOWLEDGEMENTS</FONT></H1>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Designing BugPan Interface was not an easy task. It started with an
drop down menu displaying the user session, which on clicking
displays the respective user queries and today it stand as an
powerful web interface for data analysis of Neurophysiology
experiments. Its successful completion relies with the direct and
indirect help of many people.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	First and foremost, I would like to thank God, who made me so
capable and talented to have this opportunity to work for the
Department of Neurobiology at University of Leicester, UK.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Then, I would like to thank the most important, talented, and highly
skilled and dedicated person Dr. Tom Nielsen who corrected me at
almost every step of my project. I bugged him more than my code
bugged me, but then also he kept calm and smiling and helped me with
its utmost concern. I dedicate this project to him and I would love
to work with him again any time.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Personally, I would like to thank Dr. Tom Matheson for having me his
lab and allowing me to carry out my research for their department.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	I would also like to thank Dr. Richard Badge (co-convener) and Dr.
Ralf Schmid (convener), who arranged all the projects in different
places for all of the Msc Bioinformatics students. During the
project, they were in constant touch with the students to ensure the
trouble free research.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	I would like to thank my parents who were a major part of this
project. They gave me full support for my working and boosted my
morale, every time when I spoke to them. God bless them.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	I would also like to thank those people who made prodigious
technologies that made me to carry out research.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	Lastly, I would like to thank Ian Townson, computer department
officer who helped me with the problems for putting this project on
server. Thanks to his quick actions and response.</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
	I hope that this project will bring cheer and proud to all my
people, who trusted in me.</P>
<H1 CLASS="western" STYLE="page-break-before: always"><FONT FACE="Times New Roman, serif">7.
BIBLIOGRAPHY</FONT></H1>
<OL>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Ahsan, B., Saito, T.L., Hashimoto, S., Muramatsu, K., Tsuda, M.,
	Sasaki, A., Matsushima, K., Aigaki, T. and Morishita, S., 2009.
	MachiBase: a Drosophila melanogaster 5'-end mRNA transcription
	database. <I>Nucleic Acids Res., </I><B>37, </B>D49-53.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Altschul, S.F., Gish, W., Miller, W., Myers, E.W. and Lipman, D.J.,
	1990. Basic local alignment search tool. <I>J.Mol.Biol., </I><B>215,
	</B>403-410.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Augustsson, L., Mansell, H. and Sittampalam, G., 2008. Paradise: a
	two-stage DSL embedded in Haskell. James Hook and  Peter Thiemann,
	eds. In: <I>ICFP, </I>2008, ACM pp225-228.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Bear, M.F., Conners, B.W. and Paradiso, M.A., 1996. <I>Neuroscience:
	Exploring the Brain. </I>Baltimore: Williams \&amp; Wilkins.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Brookes, E., Demeler, B., Rosano, C. and Rocco, M., 2009. The
	implementation of SOMO (SOlution MOdeller) in the UltraScan
	analytical ultracentrifugation data analysis suite: enhanced
	capabilities allow the reliable hydrodynamic modeling of virtually
	any kind of biomacromolecule. <I>Eur.Biophys.J., </I>.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Burnett, M., Agrawal, A. and van Zee, P., 2000. Exception Handling
	in the Spreadsheet Paradigm. <I>IEEE Trans.Softw.Eng., </I><B>26,
	</B>923-942.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Christensen, T.A., 2005. <I><B>Methods in insect sensory
	neuroscience</B></I><I>. </I>[e-book]. Florida: CRC press. Available
	from :
	http://books.google.co.uk/books?id=RBbxm3yeyMgC&amp;printsec=frontcover&amp;source=gbs_navlinks_s#v=onepage&amp;q=&amp;f=false.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Crane, D., Bibeault, B. and Locke, T., 2007. <I>Prototype and
	scriptaculous in action. </I>Greenwich, CT, USA: Manning
	Publications Co.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Durinck, S., Bullard, J., Spellman, P.T. and Dudoit, S., 2009.
	GenomeGraphs: integrated genomic data visualization with R. BMC
	Bioinformatics, <B>10, </B>2.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Dziubecki, P. and  Zola, J., 2006. <I>Grid Portal for Multiple
	Sequence Alignment.</I> Ph. D. Poznan Supercomputing and Networking
	Center.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Encyclopædia, B., 2009<I>. locust.</I> [online].  Available at:
	http://www.britannica.com/EBchecked/topic/345932/locust [accessed13
	Nov. 2009 2009].</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Eswar, N., Eramian, D., Webb, B., Shen, M.Y. and Sali, A., 2008.
	Protein structure modeling with MODELLER. <I>Methods Mol.Biol., </I><B>426,
	</B>145-159.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Flanagan, D. &amp; Ferguson, P., 1998. <I>JavaScript: The Definitive
	Guide. </I>Sebastopol, CA, USA: O'Reilly \&amp; Associates, Inc.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Gabbiani, F., Krapp, H.G. and Laurent, G., 1999. Computation of
	object approach by a wide-field, motion-sensitive neuron.
	<I>J.Neurosci., </I><B>19, </B>1122-1141.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Hornik, K., 2009. The R FAQ. 
	</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Hudak, P., 2000. <I>The Haskell School of Expression: Learning
	Functional Programming through Multimedia. </I>0th ed. Cambridge
	University Press.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Jamison, D.C., 2003. Structured Query Language (SQL) fundamentals.
	<I>Curr.Protoc.Bioinformatics, </I><B>Chapter 9, </B>Unit9.2.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Jang, D. and Choe, K., 2009. Points-to analysis for JavaScript, <I>SAC
	'09: Proceedings of the 2009 ACM symposium on Applied Computing,
	</I>2009, ACM pp1930-1937.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Johnson, D., White, A. and Charland, A., 2007. <I>Enterprise AJAX:
	Strategies for Building High Performance Web Applications. </I>Upper
	Saddle River, NJ, USA: Prentice Hall PTR.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Kandel, E.R. &amp;  Squire, L.R., 2000. Neuroscience: breaking down
	scientific barriers to the study of brain and mind. <I>Science, </I><B>290,
	</B>1113-1120.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	<SPAN LANG="de-DE">Kasten, E., HTML. </SPAN><SPAN LANG="de-DE"><I>Linux
	J., </I></SPAN><SPAN LANG="de-DE">3.</SPAN></P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Krzywinski, M., Schein, J., Birol, I., Connors, J., Gascoyne, R.,
	Horsman, D., Jones, S.J. and Marra, M.A., 2009. Circos: an
	information aesthetic for comparative genomics. <I>Genome Res., </I><B>19,
	</B>1639-1645.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Liang, C., 2004. Programming language concepts and Perl.
	<I>J.Comput.Small Coll., </I><B>19, </B>193-204.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Lipovača, M., 2009<I>. </I><I><B>Learn You a Haskell for Great
	Good!</B></I><I>.</I> [online].  Available at:
	http://learnyouahaskell.com/ [accessed12 Nov,2009 2009].</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Mangan, M.E., Williams, J.M., Kuhn, R.M. and Lathe, W.C.,3rd, 2009.
	The UCSC genome browser: what every molecular biologist should know.
	<I>Curr.Protoc.Mol.Biol., </I><B>Chapter 19, </B>Unit19.9.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Matheson, T., Rogers, S.M. and Krapp, H.G., 2004. Plasticity in the
	visual system is correlated with a change in lifestyle of
	solitarious and gregarious locusts. <I>J.Neurophysiol., </I><B>91,
	</B>1-12.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Meyer, E., 2006. <I>CSS: The Definitive Guide. </I>O'Reilly Media,
	Inc.}.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Neron, B., Menager, H., Maufrais, C., Joly, N., Maupetit, J.,
	Letort, S., Carrere, S., Tuffery, P. and Letondal, C., 2009. Mobyle:
	a new full web bioinformatics framework. <I>Bioinformatics, </I><B>25,
	</B>3005-3011.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Nielsen, T., Matheson, T. and Nilsson, H., 2009. Braincurry: A
	Domain-Specific Language for Integrative Neuroscience. 
	</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Nilsson, H., Courtney, A. and Peterson, J., 2002. Functional
	Reactive Programming, Continued, <I>Proceedings of the 2002 {ACM
	SIGPLAN} {H}askell Workshop ({H}askell'02), </I>oct 2002, ACM} Press
	pp51-64.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	<SPAN LANG="de-DE">Nix, D.A. &amp;  Eisen, M.B., 2005. </SPAN>GATA:
	a graphic alignment tool for comparative sequence analysis. <I>BMC
	Bioinformatics, </I><B>6, </B>9.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Olson, G., 2009<I>. BlackBird-Open Source JavaScript Logging
	Utility.</I> [online].  Available at:
	<FONT COLOR="#000080"><U><A HREF="http://www.gscottolson.com/blackbirdjs/"><FONT COLOR="#000000">http://www.gscottolson.com/blackbirdjs/</FONT></A></U></FONT>
	[accessed15 September 2009 2009].</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Ovcharenko, I., Nobrega, M.A., Loots, G.G. and Stubbs, L., 2004. ECR
	Browser: a tool for visualizing and accessing data from comparisons
	of multiple vertebrate genomes. <I>Nucleic Acids Res., </I><B>32,
	</B>W280-6.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Sanchez-Clark, T., 2007. <I>Web Programming Interview Questions with
	HTML, DHTML, and CSS: HTML, DHTML, CSS Interview and Certification
	Review. </I>Equity Press.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	<SPAN LANG="de-DE">Schultze, J.L. &amp;  Eggle, D., 2007.
	</SPAN>IlluminaGUI: graphical user interface for analyzing gene
	expression data generated on the Illumina platform. <I>Bioinformatics,
	</I><B>23, </B>1431-1433.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Squire, L.R., 2004. Memory systems of the brain: a brief history and
	current perspective. <I>Neurobiol.Learn.Mem., </I><B>82, </B>171-177.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	StatSoft, 200<I>9. Statistica</I>. [online].  Available at:
	<FONT COLOR="#000080"><U><A HREF="http://www.statsoft.co.uk/index.php"><FONT COLOR="#000000">http://www.statsoft.co.uk/index.php</FONT></A></U></FONT>
	[accessed12 November 2009 2009].</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm; line-height: 0.18cm">
	Stein, L., 1998. <I>Official guide to programming with CGI.pm: the
	standard for building Web scripts. </I>New York, NY, USA: John Wiley
	\&amp; Sons, Inc.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Stenger, J.E., Xu, H., Haynes, C., Hauser, E.R., Pericak-Vance, M.,
	Goldschmidt-Clermont, P.J. and Vance, J.M., 2005. Statistical
	Viewer: a tool to upload and integrate linkage and association data
	as plots displayed within the Ensembl genome browser. <I>BMC
	Bioinformatics, </I><B>6, </B>95.</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Urbanek, S., 2005. <B>Cairo - Graphics device using cairographics
	library for creating bitmap images or output.</B>. [online]. 
	Available at: <FONT COLOR="#000080"><U><A HREF="http://www.rforge.net/Cairo/index.html"><FONT COLOR="#000000"><I>http://www.rforge.net/Cairo/index.html</I></FONT></A></U></FONT>
	[accessed18 October 2009 2009].</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Wolfram and  Alpha, 2009<I>. Wolfram Alpha computational knowledge
	engine.</I> [online].  Available at: <FONT COLOR="#000080"><U><A HREF="http://www.wolframalpha.com/"><FONT COLOR="#000000">http://www.wolframalpha.com/</FONT></A></U></FONT>
	[accessedNov 14 2009 2009].</P>
	<LI><P CLASS="western" STYLE="margin-top: 0.43cm; margin-bottom: 0cm">
	Zaytsev, J., 200<I>9. Proto.Menu :: prototype based context menu</I>.
	[online].  Available at:
	<FONT COLOR="#000080"><U><A HREF="http://yura.thinkweb2.com/scripting/contextMenu/"><FONT COLOR="#000000">http://yura.thinkweb2.com/scripting/contextMenu/</FONT></A></U></FONT>
	[accessed15 October 2009 2009].</P>
</OL>
<H1 CLASS="western" STYLE="page-break-before: always"><FONT FACE="Times New Roman, serif">8.
APPENDICES</FONT></H1>
<H2 CLASS="western"><A NAME="10.1.APPENDIX I|outline"></A><FONT FACE="Times New Roman, serif">APPENDIX
I</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm"><B>EXPERIMENTAL SETUP	</B></P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; border: 1px solid #000000; padding: 0.04cm 0.14cm; line-height: 150%; page-break-after: avoid">
<U><IMG SRC="TheBugPanInterfacet_html_560d9280.png" NAME="graphics14" ALIGN=BOTTOM WIDTH=641 HEIGHT=218 BORDER=0></U></P>
<P STYLE="margin-top: 0.21cm; border: 1px solid #000000; padding: 0.04cm 0.14cm">
<I>Figure1. Real Experimental set-up defining electrophysiology
experiment on locust. Left to Right, (CRT) Cathode Ray Tube Monitor
producing a black box that increases in size and used as visual
stimuli for locust which follows a collision course with constant
velocity. Locust fixed in the modelling clay, with silver hook
electrodes in its neck. The electrodes are connected to an amplifier
which amplifies the signal and is connected to an oscilloscope, which
outputs the action potential graph recordings which are captured into
computer via analogue to digital converter for analysing.</I></P>
<P CLASS="western" ALIGN=RIGHT STYLE="margin-bottom: 0cm; line-height: 150%">
L<SPAN ID="Frame9" DIR="LTR" STYLE="float: left; width: 8.92cm; height: 6.37cm; border: 1px solid #000000; padding: 0.01cm; background: #ffffff">
	<P STYLE="margin-top: 0.21cm"><IMG SRC="TheBugPanInterfacet_html_m74381daa.jpg" NAME="graphics15" ALIGN=BOTTOM WIDTH=336 HEIGHT=158 BORDER=0><I>Figure2:
	Locust(Schistocerca gregaria) is fixed in modelling clay with silver
	hooks electrodes(blue-red wire) connected to its neck, for the
	action potential recordings.</I></P>
</SPAN>ocusts were fixed in modelling clay with the dorsal aspect of
head resting on narrow extension of clay holder such that it didn't
restrict the right eye vision and the left eye was covered with clay.
The cuticle of neck was dissected to see the cervical connectives and
locust saline was added to keep it submerged. The locust was fixed in
clay in front of CRT (cathode ray tube) monitor such that the centre
of the opened right eye was aligned to the centre of the screen and
the longitudinal body of the locust was parallel to the screen
surface. The DCMD spikes were recorded by using the bipolar silver
hook electrodes which were placed under the neck connected and was
insulated with jelly. All experiments were carried out at 21-27°C
where spikes have the largest amplitude in connective as a good
response to visual stimuli. These signals were captured into the
computer using data acquisition (analogue to digital converter) and
were analysed after for the threshold value deducing spikes.
</P>
<H2 CLASS="western"><A NAME="10.2.APPENDIX II|outline"></A><FONT FACE="Times New Roman, serif">APPENDIX
II</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P STYLE="margin-top: 0.21cm; font-style: normal; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_204ca4fc.jpg" NAME="graphics16" ALIGN=BOTTOM WIDTH=637 HEIGHT=646 BORDER=0></P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><I>Figure3. Screenshot of BugPan
Interface's Experiment Page showing default spreadsheet grid along
with various accessible options present on different menu bars.</I></P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%">
<BR>
</P>
<H2 CLASS="western"><A NAME="10.3.APPENDIX III|outline"></A><FONT FACE="Times New Roman, serif">APPENDIX
III</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_m4a3ac65f.jpg" NAME="graphics17" ALIGN=BOTTOM WIDTH=641 HEIGHT=688 BORDER=0></P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><I>Figure4. The BugPan Interface in
action running multiple queries with output being generated in the
respective cells of the sessions.</I></P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<H2 CLASS="western"><A NAME="10.4.APPENDIX IV|outline"></A><FONT FACE="Times New Roman, serif">APPENDIX
IV</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_13c90c6a.jpg" NAME="graphics18" ALIGN=BOTTOM WIDTH=642 HEIGHT=749 BORDER=0></P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><I>Figure5. Data representation options
for a current selected cell containing output for a specific query
and session.</I></P>
<H2 CLASS="western"><A NAME="10.5.APPENDIX v|outline"></A><FONT FACE="Times New Roman, serif">APPENDIX
v</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" ALIGN=JUSTIFY STYLE="margin-bottom: 0cm; line-height: 150%; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_4179b824.jpg" NAME="graphics19" ALIGN=BOTTOM WIDTH=642 HEIGHT=758 BORDER=0></P>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><I>Figure6. Extensive
graphical representation of experiment data for a complex query.
These graphs are being generated with the help of R statistical
language platform including a series of histograms and ‘xy’
scatter plots.</I></P>
<H2 CLASS="western"><A NAME="10.6.APPENDIX vi|outline"></A><FONT FACE="Times New Roman, serif">APPENDIX
vi</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_29f1d3bd.jpg" NAME="graphics20" ALIGN=BOTTOM WIDTH=642 HEIGHT=664 BORDER=0></P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><I>Figure.6 Data representation in the
tabular form with table break after every seven entries giving a
clear view of data.</I></P>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<H2 CLASS="western"><A NAME="10.7.APPENDIX vii|outline"></A><FONT FACE="Times New Roman, serif">APPENDIX
vii</FONT></H2>
<P CLASS="western" STYLE="margin-bottom: 0cm"><BR>
</P>
<P CLASS="western" STYLE="margin-bottom: 0cm; page-break-after: avoid">
<IMG SRC="TheBugPanInterfacet_html_m5d454fc0.jpg" NAME="graphics21" ALIGN=BOTTOM WIDTH=642 HEIGHT=695 BORDER=0></P>
<P STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><I>Figure7. Determining the data
contained by a particular session in the form of signals, events and
durations by clicking with mouse on the respective cell which runs
Ajax to display results in the division below. These data values<SPAN LANG="">
can be asked as queries to generate the numerical values contained in
them.</SPAN></I></P>
<P ALIGN=JUSTIFY STYLE="margin-top: 0.21cm"><BR><BR>
</P>
<P STYLE="margin-top: 0.21cm"><A NAME="_PictureBullets"></A><IMG SRC="TheBugPanInterfacet_html_7ad71b4e.png" NAME="graphics22" ALIGN=BOTTOM WIDTH=12 HEIGHT=12 BORDER=0></P>
</BODY>
</HTML>
<hr size="2.5" color="red">
END_HTML
