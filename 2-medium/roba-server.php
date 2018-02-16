<?php

/// Ricevo i dati dal javascript

if (isset($_POST['fitdata'])) { 
    $post = $_POST['fitdata'];
    $result = shell_exec('python ./fit-data.py ' . escapeshellarg(json_encode($post)));
}

elseif (isset($_POST['simudata'])) {
    $post = $_POST['simudata'];
    $result = shell_exec('python ./simulated-data.py ' . escapeshellarg(json_encode($post)));
}

/// Questo risultato verrà preso dal javascript che lo infilerà nell'html
echo $result;

?>
