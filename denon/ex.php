<!--This script is called from home.html. home.html will send two variables
{inp, sta} which are the input we want to change to and the station we are
changing. Use the $_GET to access these values. Then using the php exec()
function we run a python script, giving it the system parameters of input
and station-->
<?php
$return = exec("C:/Users/Mason/Miniconda3/python.exe ../scripts/simple_switch.py ".$_GET["inp"]." ".$_GET["sta"]);
echo $return;
?>
