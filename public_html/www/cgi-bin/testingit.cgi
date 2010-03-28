#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
# Outputs any errors to the browser window
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;

# basic html starts for outputting
#print "Content-Type: text/html";

print <<END_HTML;

<html>
<head>
<title>BugPan Interface by Sukhdeep Singh</title>
<script language="JavaScript" src="/prototype.js"></script>
<script language="JavaScript" src="/scriptaculous.js"></script>
<script>
 function autocomplete() {
new Ajax.Autocompleter ('autoCompleteTextField','menufield',
'list.html',{});
}

</script>
<input type="text" id="autoCompleteTextField"/>
<div id="menufield" class="autocomplete"></div>
<input type="button" onclick="autocomplete();">start autocomplete</input>
END_HTML

