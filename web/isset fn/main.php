<?php
include "config.php";
if(!$conn){
    die('Could not connect: '.mysqli_connect_error());
}

$sql = "INSERT INTO emp (name,salary)VALUES(?,?)";
if($stmt = mysqli_prepare($conn,$sql)){
    //Find variables to be prepared statement as parameters
    mysqli_stmt_bind_param($stmt,"si",$name,$salary);

    //Set the parameters values and execute the statement againn to insert another row
    $name = "Hema";
    $salary = 67000;
    mysqli_stmt_execute($stmt);

    //Set the  parameters values and execute the statement to insert a row
    $name = "Rohit";
    $salary = 456789;
    mysqli_stmt_execute($stmt);

    echo "Records inserted successfully";
}
else{
    echo "ERROR: Could not prepare query: $sql.".mysqli_error($link);
}

//Close stsatement
mysqli_stmt_close($stmt);

mysqli_close($link);
?>
