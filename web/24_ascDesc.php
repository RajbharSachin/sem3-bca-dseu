<!DOCTYPE html>
<html>
<body>

<?php
$Products = array("Pendrive"=>"230", "Chargers"=>"150", "Laptop"=>"5000", "Notebook"=>"240","Pencils"=>"100");
asort($Products);
foreach($Products as $x => $x_value) {
    echo "Key=" . $x . ", Value=" . $x_value;
    echo"<br>";
}
?>

</body>
</html>