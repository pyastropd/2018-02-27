<?php

/// Ricevo i dati dal javascript
$post = isset($_GET['mydata']) ? $_GET['mydata'] : null;

/// Per mandarlo al python:
$result = shell_exec('python3 ./simulated-data.py ' . escapeshellarg(json_encode($post)));

/// Questo risultato verrà preso dal javascript che lo infilerà nell'html
echo $result;

?>
