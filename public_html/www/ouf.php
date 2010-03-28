<?
/*
Written by Joe Abi Raad
http://joeabiraad.com
joe.abiraad@gmail.com

Happy Coding :D
*/
$action=trim($HTTP_GET_VARS['action']);
switch($action):
	case 'login':
		$good_email="email@gospam.biz";
		$good_pass="iwannalogin";
		$sub = trim($_POST['sub']);
		$email = trim($_POST['email']);
		$password =trim($_POST['password']);
		$sep=',';
		sleep(2); # simulating
		$msg="Email and password do not match";
		if ( $password == $good_pass ){
		   # REGISTER SESSION HERE
		   print 'success,welcome.html,lolllll';
		}
		else{
		   print 'error'.$sep.$msg;
		}
//		print 'success,index.php';
	break;
	default:
		print 'error,going somewhere ?';
endswitch;
#check if the mail is valid
function fun_isemail($strng){
 return preg_match('/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/i',$strng);
}
?>