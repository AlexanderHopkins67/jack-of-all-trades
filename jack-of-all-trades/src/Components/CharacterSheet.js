import react from "react"
import StatBar from "./StatBar.js"

export default function CharacterSheet(props) {
    const statsStyles = {
        display: "flex",
        flexDirection: "row"
    }

    return(
        <div className="cs-body">
        
        <div className="cs-stats" style={statsStyles}>
            <StatBar
                MaxVal={200}
                CurrentVal={200}
                BgColour={"140, 7, 20"}
                Height={200}
                Name="HEALTH"
            />
            <StatBar
                MaxVal={200}
                CurrentVal={200}
                BgColour={"19, 37, 207"}
                Height={200}
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