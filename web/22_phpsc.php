<?php
$Subjects = array("WTE","Computer networks", "DBMS", “English”, Python);
$arrlength = count($Subjects);

for($x = 0; $x < $arrlength; $x++) {
  echo $Subjects[$x];
  echo"<br>";
}
?>