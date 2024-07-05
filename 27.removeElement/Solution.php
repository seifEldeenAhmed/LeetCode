<?php
class Solution {

function removeElement(&$nums, $val) {
    $resArr=[];
    foreach($nums as $num){
        if($num==$val){
            continue;
        }else{
            $resArr[]=$num;
        }
    }
    $nums=$resArr;
    return count($resArr);
}
}