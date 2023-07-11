<?php

// create multidimensional array
$classRec= array(
	
	// Default key for each will start from 0
	array(1,"sachin kumar singh",93),
    array(2,"aashish kumar pathak",95),
    array(3,"hoor",91),
    array(4,"tanu",89),
    array(5,"himmi",88)
);

$records = count($classRec);
	
// Display the array information
echo "Roll No.	Student_name	Total_marks \n";

for ($row = 0; $row < $records; $row+=1){
    for ($col = 0; $col <3; $col += 1){
        echo $classRec[$row][$col]."\t\t";
    }
  echo"\n";
}
?>
