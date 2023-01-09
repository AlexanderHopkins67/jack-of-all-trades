import React from "react";
import {Link, Outlet} from "react-router-dom"
import "./Header.css"

export default function Header() {
    return(
        <>
            <div className="header">
                <h2 className="header-title">Jack of all Trades</h2>
                <nav className="nav-main">
                    <Link to={"/"}>Home</Link>
                    <Link to={"joat-dashboard"}>Play </Link>
                    <Link to={"about"}>About</Link>
                </nav>
            </div>
            <Outlet />
        </>
    )
}
