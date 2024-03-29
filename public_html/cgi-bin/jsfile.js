// Author: Sukhdeep Singh
//  email: ss533@le.ac.uk

// JavaScript file containing functions using prototype
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Getting the user details
function details() {
username = $('uname').value;
new Ajax.Updater("",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/sheet.cgi',{
	parameters:{username:username}});
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Function for printing running live clock on browser
 function GetTime() {
      window.setTimeout( "GetTime()", 1000 );
      LiveTime = new Date()
      $("time").innerHTML=LiveTime;
      }
      
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////      
// Function for reloading the whole page and any page
function resetsheet() {
window.location.reload();
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
// Function for saving the user sheet navigation history in a text file in usersheets.
function savehistory() {
			var user = prompt ("Please enter your name!");
			yn = confirm("Do you want to save your History(y/n)");
			if (yn) {
			historyfile = prompt("Please enter the filename to save your history as");
			alert(user+" Your history will be saved as "+historyfile+".txt");
			}
			else alert("Enjoy your time "+user);
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Function for saving the auser queries.
var savecheck;
function savecheck() {
var username = prompt("Your name please!");
var filename = prompt("filename to save sheet as");

alert("Hello "+username+"! "+"\nYour sheet will be saved as "+filename+".txt");
for (savecheck=1;savecheck<=colcount;savecheck++) {
var userquery=$("userquery"+savecheck).value;
new Ajax.Request('http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/savesheet.cgi', {
	parameters : {username:username,userquery:userquery,filename:filename},
	onSuccess: function(resp) {eval(resp.responseText);}});
	}
savedfilesreloading();
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// function for automatically reloading the userfiles once saved
function savedfilesreloading() {
window.setTimeout("savedfilesreloading()",15000);
	new Ajax.Updater("userfiles",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/loaduserfiles.cgi',{
	parameters:{}});
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Function to download user query files
function downloading() {
var selectedfile = $("download_chooser").value;
	new Ajax.Updater("",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/download.cgi', {
	parameters : {selectedfile:selectedfile,columncount:colcount}});
	Effect.SwitchOff('userfiles');
	//new Ajax.Updater("main",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/sheet.cgi', {
	//parameters : {}});
	//document.download.reset();
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// function to open the sheet navigation history files
function downloadhistoryfile() {
var selectedhistoryfile = $("historyfilechooser").value;
window.location.href="userhistory/"+selectedhistoryfile;
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// function to download xls files which saves the session names (experiments) and module names
function downloadxlsfile() {
var selectedxlsfile = $("xlsfileschooser").value;
window.location.href="xls/"+selectedxlsfile;
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// function for detailed user query when user clicks on the hyperlink generated in response for first user query using Ajax.Updater
// *I am not sure whether i am using this funtion or not*
function askQuery() {
query=$("queryString").value;
	new Ajax.Updater('showQuery','http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/ask3.cgi', {
	parameters : {query:query,session:sessionName}});
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Autocompleter function using scriptaculous.js

 function autocomplete() {
new Ajax.Autocompleter ('autoCompleteTextField','menufield',
'list.html',{});
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Renew Function for filtering the user query
function renew() {
var query = $("renewbox").value;
new Ajax.Updater("renew",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/filter.cgi', {
	parameters : {query:query}});
new Ajax.Updater("",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/ask2.cgi', {
	parameters : {query:query}});

}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Opening sessions2.cgi on the main sheet.cgi page
function detailask(x,y,z,t) {
//var temp=new Array();
//temp=x.split(',');
var query=x;
var session=y;
var sessionfolder=z;
var plotfile=t;
var file = 'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/sessions2.cgi?session='+session+'&query='+query+'&sessionfolder='+sessionfolder+'';
new Ajax.Updater("detailask",file,{
	parameters:{session:session,query:query,sessionfolder:sessionfolder,plotfile:plotfile}});
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// function for saving the sheet experiments and modules as xls
function saveasxls() {
//var xlsfile = prompt("Please enter the name of xls file");
var xlsfile = prompt("Please enter the your .xls filename!");
	for (var checkthis=0;checkthis<numberofRows;checkthis++){
		new Ajax.Updater("",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/saveasxls.cgi',{
		parameters:{session:sessionName[checkthis],module:module[checkthis],xlsfile:xlsfile}});
	}
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function bugshot() {
	new Ajax.Updater('detailask','http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/bugshot.cgi',{
	parameters:{}});
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function debugInfo(message) {
	$("debug_info").innerHTML=message;
	$("debug_info").style.border="3px solid red";
	setTimeout( function() {$("debug_info").style.border="none";} , 1000)
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// googlebox to work on so as to retrieve google results on sheet
function googlebox() {
var googlequery = $("googlebox").value;
googlerequest='http://www.google.co.uk/search?q='+googlequery+'';
	new Ajax.Updater("autoCompleteMenu",'',{
	parameters:{query:googlequery}});
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
/***********************************************
* Highlight Table Cells Script- © Dynamic Drive DHTML code library (www.dynamicdrive.com)					*
* Visit http://www.dynamicDrive.com for hundreds of DHTML scripts										*
* This notice must stay intact for legal use																*
***********************************************/

//Specify highlight behavior. "TD" to highlight table cells, "TR" to highlight the entire row:
var highlightbehavior="TD"

var ns6=document.getElementById&&!document.all
var ie=document.all

function changeto(e,highlightcolor){
source=ie? event.srcElement : e.target
if (source.tagName=="TABLE")
return
while(source.tagName!=highlightbehavior && source.tagName!="HTML")
source=ns6? source.parentNode : source.parentElement
if (source.style.backgroundColor!=highlightcolor&&source.id!="ignore")
source.style.backgroundColor=highlightcolor
}

function contains_ns6(master, slave) { //check if slave is contained by master
while (slave.parentNode)
if ((slave = slave.parentNode) == master)
return true;
return false;
}

function changeback(e,originalcolor){
if (ie&&(event.fromElement.contains(event.toElement)||source.contains(event.toElement)||source.id=="ignore")||source.tagName=="TABLE")
return
else if (ns6&&(contains_ns6(source, e.relatedTarget)||source.id=="ignore"))
return
if (ie&&event.toElement!=source||ns6&&e.relatedTarget!=source)
source.style.backgroundColor=originalcolor
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Popup menus for the help of various options installed at Bugpan interface.
// Popup1 for filter text box.
function popup1() {
alert("Filter text box provides the user to filter out the sessions which respond true for the corresponding user query for which the filter option is being run.");
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Popup2 for Introduction of Developer marquee.
function popup2() {
alert("Sukhdeep Singh is a young Bio-Informatician with Masters in Bio-Informatics from University of Leicester,UK. His main interests are developing web-interfaces and data handling for almost all kinds of experiments that are being conducted on daily basis all around the globe. Contact : vanbug@gmail.com")
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function runbugpan() {
new Ajax.Updater ("runbugpan",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/runbugpan.cgi',{
parameters:{}});
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
function runbugpanoption() {
var runoption = $("runbugpanoption").value;
new Ajax.Updater("runbugpan",'http://bioinf3.bioc.le.ac.uk/~ss533/cgi-bin/runbugpan.cgi',{
parameters:{runoption:runoption}});
}
