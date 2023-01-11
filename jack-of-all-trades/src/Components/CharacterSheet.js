import react from "react"
import StatBar from "./StatBar.js"

export default function CharacterSheet(props) {
    const bodyStyles = {
        backgroundColor: "rgba(209, 202, 194, 1)",
        margin: 10,
        width: "50%",
        height: "100%",
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",

    }
    
    const statsStyles = {
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
        
        <div className="cs-stats" style={statsStyles}>
            <StatBar
                MaxVal={200}
                CurrentVal={200}
                BgColour={"140, 7, 20"}
                Height={"90%"}
                Name="HEALTH"
            />
            <div className="cs-portrait" style={portraitStyles}>

            </div>
            <StatBar
                MaxVal={200}
                CurrentVal={200}
                BgColour={"19, 37, 207"}
                Height={"90%"}
                Name="ENERGY"
            />
        </div>
        <div className="cs-attributes">

        </div>
        <div className="cs-actions">
        
        </div>
        <div className="cs-level">
        
        </div>
    </div>
)}