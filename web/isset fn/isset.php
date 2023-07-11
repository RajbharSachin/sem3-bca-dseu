// To check if a variable is declared or not
<?php
include "config.php";

    if(isset($_POST['Login'])){
        $n1 = $_POST["name"];
        $n2 = $_POST["password"];

    $sql = "SELECT * FROM emp where name='$n1' AND password='$n2'";
    $result = mysqli_query($conn, $sql);
        if(mysqli_num_rows($result)==1){
            echo "login successful";
        }
        else{
        echo "Wrong Username or Password";
        }
}
mysqli_close($conn);
?>