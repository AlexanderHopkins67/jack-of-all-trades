import React from "react";
import axios from "axios";

export default function ActionHub() {


    function getAvailableActions() {
        axios({
            method: "GET",
            url: "/api/gameData/get",
        })
    }
    
    return(
        <div>
            
        </div>
    )
}