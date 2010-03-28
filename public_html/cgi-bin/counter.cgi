#! /usr/bin/perl
######################################################################
# Basic Graphical Counter                 Version 1.0                #
# Copyright 1999 Frederic TYNDIUK (FTLS)  All Rights Reserved.       #
# E-Mail: tyndiuk@ftls.org                Script License: GPL        #
# Created  ??/??/97                       Last Modified 05/30/99     #
# Scripts Archive at:                     http://www.ftls.org/cgi/   #
######################################################################
# Function :                                                         #
# This Script is a little graphical counter                          #
# This is my First CGI program...                                    #
######################################################################
##################### license & copyright header #####################
#                                                                    #
#                Copyright (c) 1999 by TYNDIUK Frederic              #
#                                                                    #
#  This program is free software; you can redistribute it and/or     #
#  modify it under the terms of the GNU General Public License as    #
#  published by the Free Software Foundation; either version 2 of    #
#  the License, or (at your option) any later version.               #
#                                                                    #
#  This program is distributed in the hope that it will be useful,   #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of    #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     #
#  GNU General Public License for more details.                      #
#                                                                    #
#  You should have received a copy of the GNU General Public License #
#  along with this program in the file 'COPYING'; if not, write to   #
#  the Free Software Foundation, Inc., 59 Temple Place - Suite 330,  #
#  Boston, MA 02111-1307, USA, or contact the author:                #
#                                                                    #
#                              TYNDIUK Frederic <tyndiuk@ftls.org>   #
#                                       <http://www.ftls.org/>       #
#                                                                    #
################### end license & copyright header ###################
######################################################################
# Necessary Variables:                                               #
# The following variables should be set to define the locations      #
# and URLs of various files, as explained in the documentation.      #

	# URL of gif digits
	$digits_basedir = "http://www.hostname.dom/images/Digits/";

	# Real path and file of counter
	$count_file = "/Absolute/path/to/count.txt";
	
# Nothing Below this line needs to be altered!                       #
######################################################################

($place, $Write) = split(/\&/,$ENV{QUERY_STRING});

open(COUNT,"$count_file") || die "Can't Open Count File $count_file, Error : $!\n"; 
($count) = <COUNT>;
close(COUNT);
$count =~ s/\n//;

if ($Write =~ /w/i) {
   $count++;
   open(COUNT,">$count_file") || die "Can't Write Count File $count_file, Error : $!\n";
   print COUNT "$count";
   close(COUNT);
}
$count = "0000000000".$count;
@chiffres = split(//, $count);
@chiffres = reverse(@chiffres);
print "Location: ".$digits_basedir.$chiffres[$place].".gif\n\n";
