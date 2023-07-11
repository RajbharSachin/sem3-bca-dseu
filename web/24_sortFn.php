
<?php
$price = array("Keyboard"=>"999", "Mouse"=>"370", "Monitor"=>"5099","Ups"=>"2000","CPU"=>"24000");
krsort($price);

foreach($price as $x => $x_value) {
  echo "Key=" . $x . ", Value=" . $x_value;
  echo "\n";
}
?>

