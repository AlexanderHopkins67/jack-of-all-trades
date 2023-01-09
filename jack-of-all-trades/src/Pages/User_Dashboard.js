import React from "react";
import "./User_Dashboard.css"
import { useNavigate } from "react-router-dom";

export default function User_Dashboard() {
    const navigate = useNavigate()
    return(
        <div className="uDash-main">
            <div className="uDash-campaigns">
                <h1>Campaigns</h1>
                <hr 
                    style={{
                        color: "black",
                        backgroundColor: "grey",
                        width: "75vmin"
                    }}
                />
            </div>
            <div className="uDash-createNjoin">
                <button>Create a Campaign</button>
                <button>Join a Campaign</button>
            </div>
            <div className="uDash-characters">
                <h1>Characters</h1>
                <hr 
                    style={{
                        color: "black",
                        backgroundColor: "grey",
                        width: "75vmin"
                    }}
                />
                <div 
                className="characters-new"
                onClick={() => navigate("/joat-dashboard/character-creation")}
                >
                    <h2>+ Create New Character</h2>
                </div>
            </div>
        </div>
    )
}