#!/usr/bin/perl

# loading usual development settings/
use strict;
#use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

################################################################################
# decalarations
my $q = new CGI;
my $query = $q -> param('query');
my $session = $q -> param('session');
my $sessionfolder = $q->param('sessionfolder');
my $plothtmlfile=$q->param('plotfile');
my $wantedplothtmlfile="bugpandata/ecVoltage/$sessionfolder/$plothtmlfile";
my $querytype1;
my $querytype2;
my $bugask1;
my $bugask2;
my @bugask1;
my @bugask2;
my $firstnumber;
my $secondnumber;
my $associatedevent;
my $duration;
my $eventTime;
my $realEventTime;
my $realEventValue;
my $unitduration1;
my $unitduration2;
my $unitdurationinterval;
my @firstnumber;
my @secondnumber;
my @associatedevent;
my @duration;
my @eventTime;
my @unitduration1;
my @unitduration2;
my @unitdurationinterval;
my @realEventTime;
my @realEventValue;
my $i=0;
my $Duration=">/var/www/cgi-bin/bugpandata/Duration.txt";# Need to put either '>' or '>>' for writing once or appending to the respective file.
my $RDuration=">/var/www/cgi-bin/bugpandata/RDuration.R";
my $eventfile=">/var/www/cgi-bin/bugpandata/eventfile.txt";
my $Reventfile=">/var/www/cgi-bin/bugpandata/Reventfile.R";
my $realEventfile=">/var/www/cgi-bin/bugpandata/realEventfile.txt";
my $RrealEventfile=">/var/www/cgi-bin/bugpandata/RrealEventfile.R";
my $unitDuration=">/var/www/cgi-bin/bugpandata/unitDuration.txt";
my $RunitDuration=">/var/www/cgi-bin/bugpandata/RunitDuration.R";
my $pathis=`pwd `;
my $remove=`rm /var/LocustBrain/www/cgi-bin/bugpandata/*`;
my $ls=`ls`;
my $willchangeit;
my $plotcounter =1;
# Ending Declarations
################################################################################
# Opening some required file handles
open(AL,$Duration);
open(RAL,$RDuration);
open(EF,$eventfile);
open(REF,$Reventfile);
open(ER,$realEventfile);
open(RER,$RrealEventfile);
open(UD,$unitDuration);
open(RUD,$RunitDuration);
open(PF,$wantedplothtmlfile);
my @plothtmlfile=<PF>;
################################################################################
# basic html starts for outputting
    print "Content-Type: text/html\n\n";
    @bugask1 = `bugsess ask1 $session '$query'`;
    @bugask2 = `bugsess ask1 $session '$query' -g  2>/dev/null`;
            print $remove;
    print "<h4><center><b style='color:#008000'>Session Selected is <b style='color:#B22222'>'$session'</b> for query <b style='color:#B22222'>'$query'</b></b></center></h4>";
    print "<hr size='2.5'>";
################################################################################
# fetching the query type which can be 'Event', 'Duration' or a signal but signal is not defined in out experiment
# $querytype1 defines the query type and $querytype2 defines the real,string,int or an empty value i.e ().
    foreach $bugask2(@bugask1){
    if ($bugask2=~/\w+\s+=\s+(.+)\s(.+)/){
    $querytype1=$1;
    $querytype2=$2;
    last;
    }
    }
################################################################################
# querytype output being defined for Events i.e. 'tStart', 'tStop' which have empty values
if ($querytype1 eq "Events" && $querytype2 eq "()") {
    foreach $bugask1(@bugask1){
        if ($bugask1=~/^\((\d+.\d+),\(\)/) {
            $eventTime[$i]=$1;
            print (EF "$eventTime[$i]\n");
            $i++;
        }
    }
     print "<center><b style='color:#008000'>Some Graphical Information</center>";
     print (REF "eventTime<-data.matrix(read.delim('/var/www/cgi-bin/bugpandata/eventfile.txt'))\nrequire(Cairo)\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/eventTime.png\")\nhist(eventTime,col=\"BurlyWood\",50,xlab=\"$query Event Times\")\ndev.off()\n");
     `R --vanilla --slave</var/www/cgi-bin/bugpandata/Reventfile.R`;
     # LightBox is used here for the image display on the same page in a nice style.
     print "<br></b><center><a href=\"bugpandata/eventTime.png\" rel=\"lightbox\"><img src=\"bugpandata/eventTime.png\"></a></center>";
     print "</img><br>";
     print "<hr size=2.5>";
     print @bugask1;
}
################################################################################
# querytype ouyput being defined for the 'Event Real()' such as realEvt.
if ($querytype1 eq "Events" && $querytype2 eq "Real") {
foreach $bugask1(@bugask1){
        if ($bugask1=~/^\((\d+.\d+),(.+)\)/) {
            $realEventTime[$i]=$1;
            $realEventValue[$i]=$2;
            print (ER "$realEventTime[$i]\t$realEventValue[$i]\n");
            $i++;
        }
    }
     print "<center><b style='color:#008000'>Some Graphical Information</center>";
     print (RER "realEvent<-read.delim('/var/www/cgi-bin/bugpandata/realEventfile.txt')\nrealEventTime<-data.matrix(realEvent[1])\nrealEventValue<-data.matrix(realEvent[2])\nrequire(Cairo)\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/realEventTime.png\")\nhist(realEventTime,col=\"BurlyWood\",50,xlab=\"$query Event Times\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/realEventValue.png\")\nhist(realEventValue,col=\"BurlyWood\",50,xlab=\"$query Event Values\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/eventxyscatter.png\")\nplot(realEventValue~realEventTime,data=realEvent,col=\"GoldenRod\")\ntitle(main=\"Scatter Plot b/w \nreal Event Time & Value\")\nabline(lm(realEventValue~realEventTime,data=realEvent),col=\"BlanchedAlmond\")\ndev.off()");
     `R --vanilla --slave</var/www/cgi-bin/bugpandata/RrealEventfile.R`;
     # LightBox is used for the collection of images(graphs) which can be scrolled via keyboard.
     print "<br></b><a href=\"bugpandata/realEventTime.png\" rel=\"lightbox[EventReal]\"><img src=\"bugpandata/realEventTime.png\"/></a>";
     print "<a href=\"bugpandata/realEventValue.png\" rel=\"lightbox[EventReal]\"><img src=\"bugpandata/realEventValue.png\"></a>";
     print "<a href=\"bugpandata/eventxyscatter.png\" rel=\"lightbox[EventReal]\"><img src=\"bugpandata/eventxyscatter.png\"></a>";
     print "</img><br>";
     print "<hr size=2.5>";
     print "@bugask1";
    }
################################################################################
# querytype output being defined for empty values or null values which are signals in our experiment as they are not defined
elsif ($querytype1 eq "") {
## outputs the query result
    print "<kbd> @bugask2 </kbd>";
## generates the plots for the signal ('ecVoltage')
    foreach $willchangeit(@plothtmlfile) {
    if ($willchangeit=~/<img\s+(\w+="\/\w+\/\w+\/\w+\/\w+\/(.+\..+)"\s+)/){
    print "<center><b style='color:#008000'>Plot Number : $plotcounter</b>";
    print "<br><a href='bugpandata/ecVoltage/$sessionfolder/$2' rel ='lightbox[signals]'><img src='bugpandata/ecVoltage/$sessionfolder/$2'></img></a></center>";
    $plotcounter=$plotcounter+1;
    }
    }
    $plotcounter=$plotcounter-1;
## outputs the number of plots generated on the browser
    print "<center><b style='color:#1980AF'>Total Number of Plots generated = $plotcounter</center>";
}
################################################################################
# querytype output being defined for Duration which can be Int, String or Real. String can't be used as they are not numbers
    elsif ($querytype1 eq "Durations" && $querytype2 eq "Real"){ # Real after duration means that a number value is associated with that
## generates a text file which containes all the information about different values of ecVoltage named as Duration.txt.
        foreach $bugask1(@bugask1){
            if ($bugask1=~/\(\((\d+\.\d*),(\d+\.\d*)\),(.+)\)/){
                $firstnumber[$i]=$1;
                $secondnumber[$i]=$2;
                $duration[$i]=$secondnumber[$i]-$firstnumber[$i];
                $associatedevent[$i]=$3;
                print (AL "$firstnumber[$i]\t$secondnumber[$i]\t$duration[$i]\t$associatedevent[$i]\n");
                $i++;
            }
        }
## it removes all the graphs of ecVoltage before creating them
     print "<center><b style='color:#008000'>Some Graphical Information</center>";
## it creates an R instruction file for generating the histograms by R
    print (RAL "Duration<-read.delim('/var/www/cgi-bin/bugpandata/Duration.txt',header=TRUE)\nnames(Duration)<-c(\"Starttimes\",\"Endtimes\",\"Duration\",\"Values\")\nDurationStartTimes<-data.matrix(Duration[1])\nDurationEndTimes<-data.matrix(Duration[2])\nDurationReal<-data.matrix(Duration[3])\nDurationValues<-data.matrix(Duration[4])\nrequire(Cairo)\nCairoPNG(\"/var/www/cgi-bin/bugpandata/DurationStartTime.png\")\nhist(DurationStartTimes,col=\"BurlyWood\",50,xlab=\"$query Start Times\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/DurationEndTime.png\")\nhist(DurationEndTimes,col=\"IndianRed\",50,xlab=\"$query End Times\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/Duration.png\")\nhist(DurationReal,col=\"yellow\",xlab=\"Duration of $query\",50)\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/DurationValues.png\")\nhist(DurationValues,50,col=\"brown\",xlab=\"Values associated with $query\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/durationxyscatter.png\")\nplot(DurationEndTimes~DurationStartTimes,data=Duration,col=\"GoldenRod\")\ntitle(main=\"Scatter Plot for start and end times\")\nabline(lm(DurationEndTimes~DurationStartTimes,data=Duration),col=\"BlanchedAlmond\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/startdurxyscatter.png\")\nplot(DurationValues~DurationStartTimes,data=Duration,col=\"GoldenRod\")\ntitle(main=\"Scatter Plot for \nstart time and associated value\")\nabline(lm(DurationValues~DurationStartTimes,data=Duration),col=\"BlanchedAlmond\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/stopdurxyscatter.png\")\nplot(DurationValues~DurationEndTimes,data=Duration,col=\"GoldenRod\")\ntitle(main=\"Scatter Plot for \nend time and associated value\")\nabline(lm(DurationValues~DurationEndTimes,data=Duration),col=\"BlanchedAlmond\")\ndev.off()");
## it commences the R instruction file which is being saved as RDuration.R
    `R --vanilla --slave -q</var/www/cgi-bin/bugpandata/RDuration.R`;
## it generates the image on browser so that the user can view them
    print "</b><br><a href=\"bugpandata/DurationStartTime.png\" rel=\"lightbox[Durations]\"><img src='bugpandata/DurationStartTime.png' width=\"280\" height=\"325\",></a>";
    print "<a href=\"bugpandata/DurationEndTime.png\" rel=\"lightbox[Durations]\"><img src='bugpandata/DurationEndTime.png'></a>";
    print "<a href=\"bugpandata/Duration.png\" rel=\"lightbox[Durations]\"><img src='bugpandata/Duration.png'></a>";
    print "<a href=\"bugpandata/DurationValues.png\" rel=\"lightbox[Durations]\"><img src='bugpandata/DurationValues.png'></a>";
    print "<a href=\"bugpandata/durationxyscatter.png\" rel=\"lightbox[Durations]\"><img src='bugpandata/durationxyscatter.png'></a>";
    print "<a href=\"bugpandata/startdurxyscatter.png\" rel=\"lightbox[Durations]\"><img src='bugpandata/startdurxyscatter.png'></a>";
    print "<a href=\"bugpandata/stopdurxyscatter.png\" rel=\"lightbox[Durations]\"><img src='bugpandata/stopdurxyscatter.png'></a>";
    
    print "</img><br>";
    print "<hr size=2.5>";
## this command generates the query result below the histograms
    print @bugask1; # All values
    }
################################################################################
# querytype output being defined for Duration which has empty value associated with it i.e. '()'
    elsif ($querytype1 eq "Durations" && $querytype2 eq "()"){ # Empty bracket after duration means no value is associated with that.
     foreach $bugask1(@bugask1){
            if ($bugask1=~/\(\((\d+\.\d*),(\d+\.\d*)\),.+\)/){
            $unitduration1[$i]=$1;
            $unitduration2[$i]=$2;
            $unitdurationinterval[$i]=($unitduration2[$i]-$unitduration1[$i]);
            print(UD "$unitduration1[$i]\t $unitduration2[$i]\n");
            $i++;
    }
    }
     print "<center><b style='color:#008000'>Some Graphical Information</center>";
     print (RUD "unitDuration<-read.delim('/var/www/cgi-bin/bugpandata/unitDuration.txt')\nunitDurationStartTimes<-data.matrix(unitDuration[1])\nunitDurationEndTimes<-data.matrix(unitDuration[2])\nrequire(Cairo)\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/unitDurationStartTimes.png\")\nhist(unitDurationStartTimes,col=\"BurlyWood\",50,xlab=\"$query Event Times\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/unitDurationEndTimes.png\")\nhist(unitDurationEndTimes,col=\"BurlyWood\",50,xlab=\"$query Event Times\")\ndev.off()\nCairoPNG(width=280,height=325,\"/var/www/cgi-bin/bugpandata/unitDurationxyscatter.png\")\nplot(unitDurationEndTimes~unitDurationStartTimes,data=unitDuration,col=\"GoldenRod\")\ntitle(main=\"Scatter Plot for start and end times\")\nabline(lm(unitDurationEndTimes~unitDurationStartTimes,data=unitDuration),col=\"BlanchedAlmond\")\ndev.off()");
     `R --vanilla --slave</var/www/cgi-bin/bugpandata/RunitDuration.R`;
     print "<br></b><a href=\"bugpandata/unitDurationStartTimes.png\" rel=\"lightbox[DurationEmpty]\"><img src=\"bugpandata/unitDurationStartTimes.png\"></a>";
     print "<a href=\"bugpandata/unitDurationEndTimes.png\" rel=\"lightbox[DurationEmpty]\"><img src=\"bugpandata/unitDurationEndTimes.png\"></a>";
     print "<a href=\"bugpandata/unitDurationxyscatter.png\" rel=\"lightbox[DurationEmpty]\"><img src=\"bugpandata/unitDurationxyscatter.png\"></a>";
     print "</img><br>";
     print "<hr size=2.5>";
     print @bugask1;
    }
################################################################################
## an else condotion for the rest of cases which includes the outputting of errors as well.
    else{
    print @bugask1;
    }
    print "<hr size=2.5>";
################################################################################
# script ends
################################################################################
