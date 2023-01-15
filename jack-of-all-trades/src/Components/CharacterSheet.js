import react, { useState } from "react"
import StatBar from "./StatBar.js"
import ActionHub from "./ActionHub.js"
import axios from "axios"

export default function CharacterSheet(props) {
    const [playerHealth, setPlayerHealth] = useState(200)

    function RandomHealth() {
        // newVal = Math.floor(Math.random() * 200)
        axios({
            method: "POST",
            url: "/api/authTest",
            headers: {
                'x-access-token': sessionStorage.getItem("sessionToken")
            }
        })
        .then((response) => {
            console.log(response)
        })
    }


    const bodyStyles = {
        backgroundColor: "rgba(209, 202, 194, 1)",
        margin: 10,
        width: "50%",
        height: "100%",
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",

    }
    
    const mainInfoStyles = {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        height: 200
    }

    const portraitStyles = {
        height: "70%",
        width: 100,
        backgroundColor: "white",
        border: "2px solid black",
        borderRadius: "25% 25% 0 0"
    }

    return(
        <div className="cs-body" style={bodyStyles}>
        
        <div className="cs-mainInfo" style={mainInfoStyles}>
            <StatBar
                MaxVal={200}
                CurrentVal={playerHealth}
                BgColour={"140, 7, 20"}
                Height={"90%"}
                Name="HEALTH"
            />
            <button onClick={RandomHealth}>Random Health</button>
            <div className="cs-portrait" style={portraitStyles}>

            </div>
            <StatBar
                MaxVal={200}
                CurrentVal={200}
                BgColour={"19, 37, 207"}
                Height={"90%"}
                Name="ENERGY"
            />
            <div className="cs-actions">
                <ActionHub
                isHostile={false}
                 />
            </div>
        </div>
        <div className="cs-attributes">

        </div>
    </div>
)}