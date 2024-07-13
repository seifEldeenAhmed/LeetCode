<?php 


function removeDuplicates(&$nums) {
    $freqArr= [];

    foreach($nums as $key=>$int){
        if($freqArr[$int]){
            $freqArr[$int]++;
            if($freqArr[$int]>2){
                unset($nums[$key]);
            }
        }else{
            $freqArr[$int]=1;
        }
    }
}