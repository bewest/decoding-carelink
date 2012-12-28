<?
// print_r(arguments($argv));

  $parts = arguments($argv);
  $filename = $parts["arguments"][0];
  print "filename=$filename\n";
  $f1 = fopen($filename,"rb");

while ( ($buf=fread( $f1, 8192 )) != '' ) {
     // Here, $buf is guaranted to contain data
     $contents .= $buf;
 }
 if($buf===FALSE) {
     echo "THERE WAS AN ERROR READING\n";
 }

  fclose($f1);

  $len = strlen($contents);
   print "Length of read is $len\n";

$byte_array = unpack('C*', $contents);
//print_r($byte_array);

  $i = 4;
  while($i<= $len){
       // print $byte_array[$i] . " ";
      //if($i%40==0) print "\n";

       $pattern = 0;
//Patterns to pull out
//123 0 0 0 3 0 0 0 128
//123 0 0 0 6 0 0 0 128 0 0 0 30 0 0 0 20 0 0 0 12 0 0 0 11 0 0 0 41 0 0 0 39 0 0 0 0 0 0 0 
      if($byte_array[$i]=="123" && $byte_array[$i + 8]=="128") {
         $pattern = 1;
         print "\n\n\n";
         $recordsize = 40;
         $j = 0;
         while($j < $recordsize ) {
           $pointer = $i + $j;
            print $byte_array[$pointer] . "|";
            $j += 1;
            }
         print "\nRECORD: BASIL PROFILE \n";
         print "INDEX=" . $byte_array[$i+4] . "\n";
         print "START_MINUTES=" . $byte_array[$i+12] . "\n";
         print "START_HOUR=" . $byte_array[$i+16] . "\n";
        $ssecs = (3600*1000*$byte_array[$i+16]) + (60*1000* $byte_array[$i+12]) ;
         print "INTERPRETED TIME:  " . doubleoh($byte_array[$i+16]) . ":" . doubleoh($byte_array[$i+12]) .  " SPREADSHEET SECONDS= " . $ssecs  . "\n";
         print "START_DAY_OF_MO=" . $byte_array[$i+20] . "\n";
         print "START_YEAR=" . "20" . $byte_array[$i+24] . "\n";
         print "UNKNOWN VALUE=" . $byte_array[$i+28] . "\n";
         print "RAW RATE=" . $byte_array[$i+32] . " TRANSLATES to " . $byte_array[$i+32] * 25 .  "\n";
         print "\n";
         $i = $pointer + 1;
       }
//Patterns to pull out
//123 0 0 0 3 0 0 0 128
//123 0 0 0 6 0 0 0 128 0 0 0 30 0 0 0 20 0 0 0 12 0 0 0 11 0 0 0 41 0 0 0 39 0 0 0 0 0 0 0 
      if($byte_array[$i]=="5" && $byte_array[$i + 4]=="5"  && $byte_array[$i + 4]=="4")  {
         $pattern = 1;
         print "\n\n\n";
         $recordsize = 40;
         $j = 0;
         while($j < $recordsize ) {
           $pointer = $i + $j;
            print $byte_array[$pointer] . "|";
            $j += 1;
            }
         print "RECOGNIZED 554\n";
         $i = $pointer + 1;
       }
      if($pattern==0) {//no pattern detected
        print $byte_array[$i] . "|";
        $i +=  4;
       }//no pattern
  }//while


function doubleoh($number){
    if($number<=9)  return("0".$number);
    return($number);
}
 
function arguments ( $args )
 {
   array_shift( $args );
   $endofoptions = false;
 
  $ret = array
     (
     'commands' => array(),
     'options' => array(),
     'flags'    => array(),
     'arguments' => array(),
     );
 
  while ( $arg = array_shift($args) )
   {
 
    // if we have reached end of options,
     //we cast all remaining argvs as arguments
     if ($endofoptions)
     {
       $ret['arguments'][] = $arg;
       continue;
     }
 
    // Is it a command? (prefixed with --)
     if ( substr( $arg, 0, 2 ) === '--' )
     {
 
      // is it the end of options flag?
       if (!isset ($arg[3]))
       {
         $endofoptions = true;; // end of options;
         continue;
       }
 
      $value = "";
       $com   = substr( $arg, 2 );
 
      // is it the syntax '--option=argument'?
       if (strpos($com,'='))
         list($com,$value) = split("=",$com,2);
 
      // is the option not followed by another option but by arguments
       elseif (strpos($args[0],'-') !== 0)
       {
         while (strpos($args[0],'-') !== 0)
           $value .= array_shift($args).' ';
         $value = rtrim($value,' ');
       }
 
      $ret['options'][$com] = !empty($value) ? $value : true;
       continue;
 
    }
 
    // Is it a flag or a serial of flags? (prefixed with -)
     if ( substr( $arg, 0, 1 ) === '-' )
     {
       for ($i = 1; isset($arg[$i]) ; $i++)
         $ret['flags'][] = $arg[$i];
       continue;
     }
 
    // finally, it is not option, nor flag, nor argument
     $ret['commands'][] = $arg;
     continue;
   }
 
  if (!count($ret['options']) && !count($ret['flags']))
   {
     $ret['arguments'] = array_merge($ret['commands'], $ret['arguments']);
     $ret['commands'] = array();
   }
 return $ret;
 }
 
exit (0)
 
/* vim: set expandtab tabstop=2 shiftwidth=2: */
?> 
?>
