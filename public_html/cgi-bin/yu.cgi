#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# my decalarations


print "Content-Type: text/html\n\n";
	print '<input type="button" value="load values" onClick="insertval();"/>';
print <<END_HTML;
<head>
<script type="text/javascript" src="jscripts/sound.js"></script>
<script src="jscripts/AC_RunActiveContent.js" type="text/javascript"></script>
<script src="jscripts/AC_ActiveX.js" type="text/javascript"></script>
</head>
<body>
				  		<script type="text/javascript">AC_FL_RunContent( 'codebase','','','flash/effet','','','movie','flash/effet','','','bgcolor','#ffffff');</script>
</body>
END_HTML
