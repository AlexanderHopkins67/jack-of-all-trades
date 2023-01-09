import React from "react";
import {Outlet} from "react-router-dom";
import GameHeader from "../Components/GameHeader";


export default function GameDashboard() {
    return(
        <>
            <GameHeader/>
            <Outlet/>
        </>
    )
        }