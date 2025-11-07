<?php
$pattern = $_GET['pattern'];
$directory = $_GET['directory'];
renameFiles($pattern, $directory);
function renameFiles($pattern, $directory) {
    // Implement rename logic here
    return $directory;
}