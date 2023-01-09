import React from "react";
import { Link } from "react-router-dom";

export default function GameHeader() {
    return(
        <nav>
            <Link to={"/"} style={{color:"lightgray"}}>Home</Link>
            <Link to={"/joat-dashboard"} style={{color:"lightgray"}}>Characters</Link>
        </nav>
    )
}