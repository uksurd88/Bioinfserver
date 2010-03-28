/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*Author : Sukhdeep Singh
email : vanbug@gmail.com
Organization : University of Leicester, United Kingdom

Description :  A script designed for migrating with in the cells of the dynamic spreadsheet via keyboard using the Keyboard Events 
assigned in the prototype library of javascript.
Usage Policy : Using this script for educational purposes is recommended but for commercial purposes it should be asked from author also 
before amending or selling. If passed, it should be passed in its original form with author's name on the top.
@CopyRight Sukhdeep Singh
*/
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
var eventchecker=0;
var gokey1;
var gokey2;
var keycheck=0;
var historyfilecheck=0;
function migrate(e) {
	debugInfo("firsttimeselect"+firsttimeselect);
	var key = e.which || e.keyCode;
	var gokey = e.which || e.keyCode; // Custom navigation started if 'GO' is pressed from the keyboard
	var display;
	if (keycheck==2) {					    // This code revises the key after every 2 key strokes
		keycheck=0;
		gokey1=null;
		gokey2=null;
	}
	 	keycheck++;
	if (gokey == "103" && keycheck== 1)  gokey1=gokey; // gokey1 and gokey2 stores the keyword 'g' & 'o'.
	if (gokey == "111" && keycheck==2)   gokey2=gokey;
	if (keycheck==2) var gocheck = (gokey1+gokey2);
	 	var querycolnumber = colcount;
	 if (gocheck == 214 ) { // gocheck activates when 'g' & 'o' key number codes add and match 214
		 currentcell ="name1"; // need to pass default currentcell and next cell id
		 nextcell	 ="name0";
		 firsttimeselect =1;
	 }
	 
	 if (eventchecker>0) firsttimeselect=1; // to remain in sheet globally
		if (firsttimeselect>0 ) {
			cellid(e);
			debugInfo("coming in");
			var rowcount = (numberofRows+2);// 2 is added because 2 rows are there of Mean and Standard Deviation
			currentcellid = currentcell.substring(0,4);
			var userqueryid  = currentcell.substring(0,9);
			var mymatch = /(\d+)/;
			var querymatch = /(\d+)$/;
			var nextcell;
			var currentcellidnumber = currentcell.match(mymatch);
			var querycurrentnumber = currentcell.match(querymatch);
			currentcellidnumber = parseInt(currentcellidnumber[0]);
			querycurrentnumber = parseInt(querycurrentnumber);
				if (historyfilecheck == 0) {
				savehistory();
				historyfilecheck=1;
				}	
				display = "I am your Virtual Navigator";
				 if (key == "37") display = "LEFT";
				 if (key == "38") display = "UP";
				 if (key == "39") display = "RIGHT";
				 if (key == "40") display= "DOWN";
				 if (key == "113") {$(currentcell).style.border = "1px solid white";$(nextcell).style.border = "1px solid white";firsttimeselect=0;} 									  			// This takes the key events out of the sheet , assigned for 'q'
				 if (key =="98") eventchecker =1;  				                		      // This takes the key events back to sheet and sheet migration is restored, assigned for 'b'
				 if (key == "99") {recalcStats();display =  "Stats Calculated";}	     // This calculates the stats, assigned for c. 
				 if (key =="114") {resetsheet();display = "Sheet Resetted";}  	   // This resets the sheet, assigned for 'r'.
				 if (key == "115") {savecheck();display = "Sheet Saved";}    		  // This saves the sheet
				 if (key == "119" && colcount>1) {
				 var ans = prompt("Which column you want to write to?");
				 $("userquery"+ans).focus();									// This takes to the userquery text box for writing query, assigned for 'w'
				 display = "Commencing UserQuery for User specified Column";
				 }
				 if (key == "119" && colcount ==1) {$("userquery"+colcount).focus();display = "Commencing UserQuery";}
				 if (key =="97" && colcount>1){
				 var ans=prompt("What column you want to select?");
				 $("userquery"+ans).select();
				 display="User inputted column number "+ans+" text selected";
				 }
				 if (key == "97" ) {$("userquery"+colcount).select();display="Text Selected";} // This selects the text for first userquery column, assigned for 'a'
				 if (key == "102"){$("renewbox").focus(); display = "Out of Sheet now, using filtering";}
				 if (key == "109") $("userquery"+colcount).blur();
				 if (key == "110") {ins(); display = "New Query Column";}	      // This makes a new column, assigned for 'n'
				 log.debug(display);
				 if (yn == "y") {
					new Ajax.Updater("navigation",'/cgi-bin/sheetnavigation.cgi',{
					parameters:{display:display,filename:historyfile}});
					}
				 else if (yn == "n") {
				 new Ajax.Updater("navigation",'/cgi-bin/sheetnavigation.cgi',{
					parameters:{display:display}});
				 }
				 //if (typeof(yn)=="undefined"){// Define it for undefined as when user presses escape
				 else {
				 new Ajax.Updater("navigation",'/cgi-bin/sheetnavigation.cgi',{
					parameters:{display:display}});
				 }
				 if (key == "38" && currentcellid != "qvry")  nextcell = currentcellid+(currentcellidnumber-1);
				 if (key == "38" && currentcellid == "qvry" && currentcellidnumber !=0) nextcell = currentcellid+(currentcellidnumber-1)+'_'+querycurrentnumber; 
				 if (key == "38" && currentcellid == "qvry" && currentcellidnumber == 0) nextcell = "userquery"+querycurrentnumber;
				 if (key == "40" && currentcellid != "qvry") nextcell = currentcellid+(currentcellidnumber+1); 	
				 if (key == "40" && currentcellid == "qvry") nextcell = currentcellid+(currentcellidnumber+1)+'_'+querycurrentnumber;
				 if (key == "40" && userqueryid == "userquery") nextcell = "qvry"+0+'_'+querycurrentnumber;
				 if (key == "37") {																		// Left Event	
					if (currentcellid == "mode") nextcell = "date"+currentcellidnumber;
					if (currentcellid == "date") nextcell = "name"+currentcellidnumber;
					if (currentcellid == "qvry" && querycurrentnumber == 1) nextcell = ("mode"+currentcellidnumber);
					if (currentcellid == "qvry" && querycurrentnumber >1) nextcell = "qvry"+currentcellidnumber+'_'+(querycurrentnumber-1);
					if (userqueryid  == "userquery") nextcell = userqueryid +(querycurrentnumber-1);
				}
				if (key == "39") {														// Right Event
					if (currentcellid == "name") nextcell = "date"+currentcellidnumber;
					if (currentcellid == "date") nextcell = "mode" + currentcellidnumber;
					if (currentcellid == "mode") nextcell = "qvry"+currentcellidnumber+'_'+(querycolnumber-(querycolnumber-1));
					if (currentcellid == "qvry") nextcell = "qvry"+currentcellidnumber+'_'+(querycurrentnumber+1);
					if (userqueryid == "userquery") nextcell = userqueryid+(querycurrentnumber+1);
					if (currentcellid =="user") alert(currentcellidnumber);
				}
				if (currentcellid == "name") {
					if (key != "39") {
					file = '/cgi-bin/migrationsessionshow.cgi';
					sessionname =$(nextcell).innerHTML;
					date ="none";
					}
					if (key == "39"){
					file = '/cgi-bin/migrationdateshow.cgi';
					sessionname = $("name"+currentcellidnumber).innerHTML;
					date = $(nextcell).innerHTML;
					}
					module = "none";
					userquery = "none";					
					}
				if (currentcellid == "date") {
					if (key == "40") sessionname = $("name"+(currentcellidnumber+1)).innerHTML;
					if (key == "38") sessionname = $("name"+(currentcellidnumber-1)).innerHTML;
					file = '/cgi-bin/migrationdateshow.cgi';
					date = $(nextcell).innerHTML;
		 			module = "none";
					if (key == "37") {
					sessionname = $("name"+currentcellidnumber).innerHTML;
					file = '/cgi-bin/migrationsessionshow.cgi';
					date ="none";
					module = "none";
					}
					if (key == "39") {
					file = '/cgi-bin/migrationmoduleshow.cgi';
					sessionname = $("name"+currentcellidnumber).innerHTML;
					date = "none";
					module = $(nextcell).innerHTML;
					}
					userquery = "none";
				}
				if (currentcellid == "mode") {
					if (key == "38") sessionname = $("name"+(currentcellidnumber-1)).innerHTML;
					if (key == "40") sessionname = $("name"+(currentcellidnumber+1)).innerHTML;
					file = '/cgi-bin/migrationmoduleshow.cgi';
					date = "none";
					module = $(nextcell).innerHTML;
					userquery = "none";
					if (key == "39") {
					sessionname = $("name"+currentcellidnumber).innerHTML;
					userquery = $("userquery"+1).value;
					file ='/cgi-bin/sessions2.cgi';
					date = "none";
					module = "none";
					}
					if (key == "37") {
					sessionname =  $("name"+currentcellidnumber).innerHTML;
					file = '/cgi-bin/migrationdateshow.cgi';
					date = $(nextcell).innerHTML;
		 			module = "none";
					}
				}
				if (currentcellid == "qvry") {
					if (key == "38" && nextcell != ("userquery"+querycurrentnumber)) sessionname = $("name"+(currentcellidnumber-1)).innerHTML;
					//if (key == "38" && newcell ==("userquery"+querycurrentnumber)) alert("hello");
					if (key == "40") sessionname = $("name"+(currentcellidnumber+1)).innerHTML;
					userquery = $("userquery"+querycurrentnumber).value;
					if (key == "39") {
					sessionname = $("name"+currentcellidnumber).innerHTML;
					userquery = $("userquery"+(querycurrentnumber+1)).value;
					}
					if (key == "37" && querycurrentnumber >1) {
					sessionname = $("name"+currentcellidnumber).innerHTML;
					userquery = $("userquery"+ (querycurrentnumber-1)).value;
					}
					file = '/cgi-bin/sessions2.cgi';
					date = "none";
					module = "none";
					{
					if (key == "37" && querycurrentnumber == 1) {
					file = '/cgi-bin/migrationmoduleshow.cgi';
					sessionname = $("name"+currentcellidnumber).innerHTML;
					module = $("mode"+currentcellidnumber).innerHTML;
					}
					}
				}
						new Ajax.Updater('detailask',file,{
						parameters:{session:sessionname,date:date,module:module,query:userquery}});
					 	 $(nextcell).style.border = "7px inset white";
						$(currentcell).style.border = "1px solid white";
					 	currentcell=nextcell;
   		eventchecker=1;
   		}
   		//else return 0;
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
