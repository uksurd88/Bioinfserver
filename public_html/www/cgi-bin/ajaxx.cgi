#!/usr/bin/perl -w
use CGI;

$query = new CGI;

$secretword = $query->param('w');
$remotehost = $query->remote_host();

print $query->header;
print "<p>The secret word is <b>$secretword</b> and your IP is <b>$remotehost</b>.</p>";
