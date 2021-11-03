<?php

require getcwd().'vendor/autoload.php';

use Dompdf\Dompdf;
use Dompdf\Options;

set_time_limit(0);

$options = new Options();
$options->setIsRemoteEnabled(true); 
$options->setIsHtml5ParserEnabled(true);
$options->setIsPhpEnabled(true);
$options->setIsJavascriptEnabled(true);
$options->setChroot(__DIR__);

$dompdf = new Dompdf($options);

$dompdf->loadHtmlFile(getcwd().'\pdf_amdpa\data.html');
$dompdf->setPaper('A4');
$dompdf->render();
$output = $dompdf->output();
file_put_contents(getcwd().'\arquivos_storage\relatorio.pdf', $output);
//$dompdf->stream('re.pdf', [true]);
