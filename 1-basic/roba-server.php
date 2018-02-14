<?php

/// Ricevo i dati dal javascript
$post = isset($_GET['mydata']) ? $_GET['mydata'] : null;

/// Dati di prova per provare la pagina PHP da sola:
//$post = '{"num1":"1.2","num2":"1","txt":"asd"}';

/// Se dal browser vedi in chiaro tutto quello che c'è scritto qua
/// dentro, allora c'è un problema col php: non è installato, oppure
/// è disattivato per la tua userdir (vedi /etc/apache2/mode-available/php*.conf)

/// Per vederlo così com'è:
//$result=$post;

/// Per vederlo così come verrà inviato al python:
//$result=escapeshellarg(json_encode($post));

/// Se vuoi farlo diventare un array PHP:
//$result = json_decode($post);
//print_r($result);

/// Per mandarlo al python:
$result = shell_exec('python3 ./script-python.py ' . escapeshellarg(json_encode($post)));

/// Questo risultato verrà preso dal javascript che lo infilerà nell'html
echo $result;

?>
