#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
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
				<li><a href="developers.cgi"><img src="images/developers.gif"><span>Developers</span></img></a></li>
				<li><a href="contactus.cgi"><img src="images/contact.gif"><span>Contact Us</span></img></a></li>		
			</ul>		
		</div>	

		 <a href="http://www.schistocerca.org/"> <div id="header-image"></div></a>
	<script language="JavaScript" src="fisheye.js"></script>
	<!--header ends-->					
	</div>

<!-- HOME page introduction starts here -->
 <hr size="1">
<p><font color="green">
<h3><center>1.1 INTRODUCTION</center></h3><br>
 <hr size="1">
\t Experimentation is the building block of various scientific inventions and discoveries. Every successful invention is linked to number of repeatable experiments behind it generating a vast amount of data which is difficult to analyze and process by the experimentar itself. Huge amounts of experiments are being done on a large scale in different fields all around the world everyday which are stored in form of databases but thier analyzation is quite difficult and complicated as compared to its generation, and the result of that is scientists are not able to analyze their own data which lead to slipage of some important discoveries from hand. Then, the data analyzation softwares, come into play which makes some ease by calculating stats for the data, making some graphical representations and linking some data but those are too complicated and costly as well as you require professional knowledge and licensing to use them effectively. For instance, ORACLE and SQL databases can be handled by a proper database management professional which spend good amount of time of their life to gain expertise in this field but what for a scientific professional such as a researcher which is working on some bio-chemical experiment and is generating data on everyday basis, its very difficult for him/her to use these professional databases as first of all he is required to learn how to access the database, storing and retrieving information. Various measures have been proposed for inspecting, visualising and  annotating large datasets from databases, but in practice most scientists use a plain spreadsheet to analyse and store their data which is a grid where different data can be written, stored and analyzed, and user can also contruct graphs, apply some mathematical functions such as calculating mean, median etc of the data. This approach is practical because it imposes  almost no constraints but it has a number of disadvantages as there are no checks on the integrity of the data. Also, it is difficult to change the  shape of the sheet for different views of the data; and the data have to be entered manually or copied and pasted from different applications, which is actually time consuming and error-prone (see eg. Augustsson 2008).
Microsoft Office provides it as MS Excel, Open Office provide it as Spreadsheet but all of them works more or less the same. This simple spreadsheet helps in numerous ways as its easy to use and learn and data can be analyzed frequently without complications, but this too has problems such as <ol><li>The data needs to be copied and pasted or needs some importing and exporting</li><li>Every time an experiment is done, the data needs to be opened in spreadsheet and analyze it which makes it cumbersome</li><li>You need to have some knowledge of working on spreadsheet so as to use functions,creating charts and graphs.</li><li>If there is some error in data you need to run the experiment again and copy the data again for analyzation</li><li>Last but not the least, you need to have spreadsheet installed on your system, you can work only offline.</li></ol> What if you can analyze data directly from the setup. What if you can run experiment and analyze directly the data from browser any where around the world. What if you want to show your experiment and results to someone.<br> We kept all these things in mind and developed BUGPAN Interface which is <i> a structured spreadsheet for neurophysiology experiments</i>. It has revolutionized the data analyzation and management. BugPan Interface is being designed for data analysis to large  datasets, where each row of it represents a recording and the columns
 properties or calculations on each recording and gives result in a new column which can be created by user. This interface is currently modified for analyzing the data being generated by the neurophysiology experiments on Locusts(test aminal) which shows its efficacy and ease to use.
 <hr size="1">
<a href="#">Top</a><br>
 <hr size="1">
 <h3><center>1.2 The Neurophysiology Experiment.</center></h3><br>
  <hr size="1">
Schistocerca gregaria aka Desert Locust is seemingly gaining its importance day by day.  Almost one-tenth of the world's human population are affected by this insect for their livelihood. Locust has the ability to fly rapidly along great distances and they have 2-5 generations per year. Locusts and Grasshoppers share the family Acrididae but they are not same. The difference lies in the fact that locust can occur in two life phases viz, solitarious(living alone) and gregarious(living in groups) whereas the grasshoppers do not show this feature.<img src="2Locust.jpeg" ALIGN="Left"/> <br><br>The sensory systems tell us the molding pressures of evolution with limpid clarity. Understanding the sensory system of organisms can help us understand the convergent evolution of sensory receptors as well as various habits of organisms. The plasticity in visual system is related to change in lifestyle of locust which is one of the sensory system. The main job of the eye is to transmit the visual world information to the brain so that it can respond accordingly which is done through the bundles fibres of optic nerves. Ganglion cells which are the cell bodies of the optic nerves are situated in the retina of the eye and send their axons to the brain. The lens of the eye focuses a rather clear inage of the visual world on the retina(sheet of photoreceptors and neurons lining the back of eye). Locust's eye is different to human eye in the terms of their position. Humans have eyes to see straight whereas locust eyes are in opposite direction of 180 degrees and he can't see straight as humans can.<br>Neuroscience is a multidisciplinary field of science which analyzes the nervous system to understand the biological basis of human thought, analysis and behaviour. It includes the study of brain, network of sensory and other nerves, spinal cord and neurons. Humans typically contain more than 100 billion neurons which are the functional units of nervous system. These different types of neurons communicate with each other for proper functioning of nervous system of body by sending electrical impulses and some chemicals known as neurotransmitters which travel across the gaps between the neurons known as synapses.<br><br><br>The expeiments were conducted on Locust (<i>Schistocerca gregaria</i>) which involved invoking an response from animal by providing an external stimuli which can be touching a body part(<i>physical stimuli</i>), playing some music (<i>auditary stimuli</i>) or making some object to approach to locust eye as it is going to hit him/her (<i>visual stimuli</i>). All these stimuli's invoke response in locust as a opening/closing of ion channels which cause the formation of action potential, which carries the signal to brain and generates the response to that stimuli and all these action potential readings are being recorded. Visual systems are mostly tuned to the signal features of natural environment specific to every animal's own lifestyle such as in birds, collision sensitive neurons signal an approaching object (Sun and Frost 1998) and in toad tectum, some neurons respond to objects that look like worms (Ewart 1997). Visual tuning also changes over time for some species such as in dragonflies when aquatic larvae develops to flying adults. So in our experiment, it has been investigated for first time that whether the visual interneuron tuning in polyphenic(arising of different phenotypes from the same genotype) locust is re-tuned in those animals which undergo a significant transformation in their life style that includes some changes in behaviour and visual input as well. (Matheson, Rogers, & Krapp, 2004).
<br><br>Our experimentation has been done on both types of locusts(Schistocera gregaria Forskall) male and female viz. Gregarious locusts (which likes to live in groups) and solitarious locusts(which likes to live in isolation).LGMD(Lobula Giant Motion Detector) is a wide-field, motion-sensitive neuron in locust's visual system that responds to objects vigoursly that approach animals on a collision course. The activity of LGMD is measured when it responds to the approaching object by measuring the activity of its post synaptic target DCMD(Descending Contralateral Movement Detector) which is present just behind it.
When an animal sees an approaching object, he can avoid collision by reacting to the object either when it is some distance away or he can react at a given time to avoid the collision by monitoring the expansion of image projected on the retina by the approaching object.(Hatsopoulos, Gabbiani, & Laurent, 1995)
<hr size="1">
<a href="#">Top</a><br>
<hr size="1">
 <h3><center>1.3 Experiment by Braincurry</center></h3><br>
 <hr size="1">
<br>We conducted the expeiments by using the Braincurry <i> A domain specific query language for integrative neuroscience developed by Tom Neilsen at Department of Biology, University of Leicester,UK.</i> Braincurry has three goals:<ul type="circle"><li>allowing expeiments and data analysis to be described in a way that is sufficiently abstract to serve as a definition </li><li>to facilitate carrying out experiments by executing such descriptions</li><li>to be directly usable by the end users.</li></ul> Braincurry is currently implemented as an embedding in Haskell(<i>functional programming language</i>), which is a highly effective tool for this kind of exploratory language design.
 Locusts were fixed in modelling clay with the dorsal aspect of head resting on narrow extension of clay holder such that it didn't restrict the right eye vision and the left eye was covered with clay. The cuticle of neck was dissected to see the cervical connectives and locust saline was added to keep it submerged. The locust was fixed in clay in front of CRT(cathode ray tube) monitor such that the centre of the opened right eye was aligned to the centre of the screen and the longitudinal body of the locust was parallel to the screen surface. The DCMD spikes were recorded by using the bipolar silver hook electrodes which were placed under the neck connected and was insulated with jelly. All the experiments were carried out at 21-27°C where the spikes have the largest amplitude in connective and have a good response to the visual stimuli. These signals were captured into the computer using analog to digital converter and were analysed after that for the threshold value in peak firing.<br> 
'bugsess ' is the query processor for the Braincurry which helps to show a list of sessions which are experiments, it helps to ask some information from an specific experiment and tells about signals, durations and events defined for an experiment. An event is defined as a specific event occured at some time and has some value associated with it, if it is a real event. A duration is a event which started at some time and got ended at some time and has some value associated with it, if it is a real duration. Empty duration i.e. Duration () has start time and an end time but no associated value. A signal is defined as list of events which has start time and an end time and there are number of values associated with it. <br>'bugsess' has four options with it : <ul type="circle"><li><b>list</b>: which lists the current sessions present in the system</li><li><b>ask</b>: let us to ask a query from a specific session </li><li><b>show</b>:lists all querries that are being defined for a particular session<ol>Querries are : <li>	ecVoltage :: Signal Real</li>
	<li>realEvt :: Event Real</li>
	<li>tStop :: Event ()</li>
	<li>collision :: Event ()</li>
	<li>tStart :: Event ()</li>
	<li>displacedLoom :: Duration ()</li>
	<li>program :: Duration String</li>
	<li>moduleName :: Duration String</li>
	<li>approachLoV :: Duration Real</li>
	<li>displacedAngle :: Duration Real</li>
</li></ol></li>
<li><b>filter</b>: it filters out the positive sessions for a specific query</li></ul>
<b>'runbugpan'</b> is another haskell module which helps to start a new experiment and once experimental setup is ready with locust on its position, we can run experiment from the command line. The duration of the experiment, voltage being produced and other parameters can be controlled effectively by the user.
<hr size="1">
<a href="#">Top</a><br>
<hr size="1">
 <h3><center>1.4 BugPan Interface -- redefining data analyzation and experimentation.</center></h3><br>
 <hr size="1">
<br>Running new experiments and data analyzation of previous ones were given a new direction by Braincurry but there was one major thing lacking which was a web interface where all the sessions can be visualized, individual querries can be run on them, the data can be analyzed on the web browser, graphs can be produced of the data generated which helps the easy characterization of data, calculating statistics such as 'mean' and 'standard deviation', running multiple querries on single session and comparing data for same or different sessions for same or different querries, saving the sheet and reverting it back later, saving the sheet in .xls format so as to be enquired in MS excel or Open Office spreadsheet for more data analysis, that all without having the knowledge of any specific thing and just with the help of few clicks.<br>
The construction of BugPan interface has revolutionized the data acquisition and management.<br> Languages and Platforms used are <ul type="circle"><li>HTML(Hypertext Markup Language)</li><li>DHTML(Dynamic Hypertext Markup Language)</li><li>XML(Extensive Markup Language)</li><li>CSS(Cascading Style Sheets)</li><li>PERL(Practical Extraction & Report Language) </li><li>CGI(Common Gateway Interface)</li><li>JavaScript(Prototype and Scriptaculous libraries)</li><li>Haskell(Functional Programming Language)</li></ul>It runs on AJAX(Asynchronous Javascript and XML) which helps to display results without reloading the page. JavaScript Prototype library is being used here for the construction of this interface widely. When the sheet is opened, it automatically loads all the sessions(experiments) which are present on the system and display them in a spreadsheet format with first column of session names, second column of date of start and third column of module name which are haskell modules in which the way of conducting experiments have been defined.
The spreadsheet is being divided into six divisions viz: <ol><li>Header and sheet links</li>
<li>User sheet options</li>
<li>Time and hide/show options.</li>
<li>Userfiles division</li>
<li>Virtual Navigator Division</li>
<li>Spreadsheet</li></ol>
Header and sheet links display the header og BugPan Interface and the links for homepage, experiment, developers page and the contact us page.
Then comes the user options which are useful to control the sheet as required by the user such as <ul type="circle"><li><b>Add</b>: when clicked, adds a new query column to the sheet where the user can write above defined querries such as tStart, tStop, approachLoV which display the results for every session in their specified column without reloading the page.</li>
<li><b>Add User Column</b>: when clicked, adds a new user column to the existing spreadsheet, where user can write some points, values or notes related to the corresponding session.</li>
<li><b>Save User File</b>: when clicked, saves the current user querries in a new user file whose name is given by the user, so that he can retrieve it later.</li>
<li><b>Calculate Statistics</b>: when clicked, calculates the statistics such as 'Mean' and 'Standard Deviation' for the values which are outputted for any standard query, if there are no numeric values, then <i>'NaN'</i></li> is displayed on the screen.
<li><b>Save as xls</b>:when clicked, saves the current sessions and module names in a new user entered .xls file, which can be viewed in any of Office's spreadsheet. </li>
<li><b>Reset</b>:when clicked, resets the sheet to the start point.</li>
</ul>
\tThe next division displays the current time and is updated per second, so that user can keep record of each second. The next line displays some hide/show options for the usersheet and the userfiles. These options use Prototype library and the whole division can be displayed or can be made hidden by pressing the respective buttons. These options include a filter text box, which is used to filter out the querries and actually runs <i>`bugsess filter query`</i>. It filters out the sessions which are true for the specific query which the user enters in the filter text box and displays them in the form of new sheet, on to which, new query columns can be added and the querries can be processed. <br>
 Next division displays the userfiles which are classified as User Sheets which store the user querries stored by the user at some time, History files which record the sheet navigation steps, and xls files which record the .xls files stored by pressing the 'Save as xls' button. The user sheets retrieval is of dynamic form such that the user needs not to rewrite the querries and need not to execute them in the respective columns, but they get automatically executed in new columns which get made automatically for the amount of querries stored in a specific file. This concept of dynamism is very realistic and is very friendly to user.<br>
<center> <h4>Sheet Navigation System(Full Keyboard Control)</h4></center>
Its very delightfull to introduce the Sheet Navigation System first time being used in BugPan Interface. It allows you to automate and have the full control of the spreadsheet via keyborad as we have in Office's Spreadsheet. When the user opens the sheet, it says <marquee><pre><center><font color="navy">Status : I am your Virtual Navigator and Status Updater
You are outside sheet now. Please type 'GO' to come to sheet.</font></center></pre></marquee>
If its been a simple html or dynamic table, you need to migrate between the column by mouse clicks, but this concept is completely automated and the full spreadsheet migration is defined by keyboard. First of all, we need to enter the sheet which can be done by pressing <i>'GO'</i> or pressing the key 'G' and then 'O', no other keypress will activate the sheet navigation system. Once the 'GO' is pressed, it asks for the username of user and then it asks whether the user want to save the history which is sheet navigation history or not and will store on the user specified file name. After the sheet is activated, the first box or cell of the sheet will get highlighted and this indicates the sheet activation. Now user can migrate to the right cell by pressing the right '->' key on the keyboard and same is being defined for the the others viz, <ul type="circle"><li>↑ -- UP </li>
<li>↓ -- DOWN</li>
<li>← -- LEFT</li>
<li>→ -- RIGHT</li>
<li>a -- selects the user query, if there are two or more columns, it asks which column you want to select.</li>
<li>c -- calculates the statistics for the values generated and displays them in thier respective boxes.</li>
<li>f --  takes the user to the filter textbox, so that some session filtering can be done.</li>
<li>n -- makes a new query column so that some user query can be commenced.</li>
<li>r -- resets the sheet to the start point.</li>
<li>s -- prompts the user for the filename and saves the sheet with that filename.</li>
<li>w-- write function, which takes the user to the userquery box where user can type in the query and if there are two or more columns, it automatically asks which column the user want to write to.</li></ul>
The best part if sheet navigation is it displays the full information for the current selected cell on the page which follows and runs on AJax(we get the results without reloading the page).
For every keyboard action, the second line of the Status for Sheet Navigator gets replaced by the which key is currently being pressed and it also displays the action associated with it such as commencing user query, left, right, up, down, saving sheet, sheet reseted etc.
All the actions done in one time by user can retrieved later at any point of time as an text file, if he saves the history as the start.
<br>The most vital part is the spreadsheet which comes now. Our spreadsheet is a grid where initially the the number of rows depend on the number of sessions or experiments and the number of columns are fixed which are three in number. The first column shows the Session Names which are alphanumeric bits generated by the haskell program and for the sake of simplicity, only first six unique characters are shown. The next column is of Start Time and tells about the date when the particular session was started and the third column shows the Module Names, which are haskell programs and they have different set of instructions to run an experiment differently and it tells which session runs which module. This default table gets generated every time, when the sheet is opened and is running a perl pattern cgi script on the back which runs <i>`bugsess show 'sessionname'`</i> on the terminal for every session and displays the results in respective columns. The session list is generated by <i>`bugsess list`</i> which are currently present on the system. When a module is made to run once, a set of values are being generated. So the number in the round parenthesis tells how much times the specific module has been run. In the default state, mean and standard deviation rows are being generated at the bottom for their future use.<br>
Now, the working of the sheet starts by pressing the add key from menu bar, or activating the sheet by pressing 'GO' and then pressing the key 'n' or the <i>protomenu</i> is being defined for this sheet as well, which gets activated when the user pointer is over the sheet. Five major options are being defined for the mouse lovers, viz, <ul type="circle"><li>Add Query Column</li><li>Add User Column</li><li>Calculate Statistics</li><li>Save Sheet</li><li>Reset Sheet</li></ul>
So, after adding a new query column, the user can write query by migrating to the userquery column via keyboard or mouse, and when he presses the enter the <i>`bugsess ask sessionname query`</i> runs for every session and the results get displayed in the form of graphs and values for the respective sessions in respective cells without reloading the page. It gives a brief view about avery session by presenting the answer in graphical way and tabular form, clicking on the cells where the output is generated, displays the full results on the page which follows it that without reloading the page, and thus detailed analysis can be performed on the data.<br>
Some modifications has been done recently, which diplays the graphical information first and values afterwards. The graphs are being generated for every session and can be viewed on the page which follows it. For the events, a single histogram is generated, for durations, four histograms are being generated for the start time, end time, duration which is the difference between the two and the histogram of the values associated. A xy-scatter is also produced for the duration which make the data analyzation easier. For the signals, if there are more than one graph, a small graph is displayed in the cell,which when clicked displays all the graphs on the page which follows for the respective sessions. The user query <i>'ploManySigs ecVoltage'</i> generates one graph for every single module run and for example, if the value in the module name is 100, then 100 graphs will be generated for the particular session or experiment.The sheet can be saved any time and an old one can be retrieved ant time which allows the comparison to be done between two of them.
<hr size="1">
<a href="#">Top</a><br>
 <hr size="1">
</p>
<a href='http://bcs.whfreeman.com/thelifewire/content/chp44/4402s.swf'>Action Potential</a></font>
Sukhi
<hr size="2.5" color="red">
END_HTML
