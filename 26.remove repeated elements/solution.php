<?php    
    $curr=null;
        foreach($nums as $key=>$value){
            if($value===$curr){
                unset($nums[$key]);
            }else{
                $curr=$value;
            }
        }
        return count($nums);