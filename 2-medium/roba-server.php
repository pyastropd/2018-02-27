<?php

/// Ricevo i dati dal javascript

if (isset($_GET['fitdata'])) { 
    $post = $_GET['fitdata'];
    $result = shell_exec('python3 ./fit-data.py ' . escapeshellarg(json_encode($post)));
}

elseif (isset($_GET['simudata'])) {
    $post = $_GET['simudata'];
    $result = shell_exec('python3 ./simulated-data.py ' . escapeshellarg(json_encode($post)));
}

/// Questo risultato verrà preso dal javascript che lo infilerà nell'html
echo $result;

?>
