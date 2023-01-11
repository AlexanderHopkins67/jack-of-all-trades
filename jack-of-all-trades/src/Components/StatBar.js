import React from "react";


export default function StatBar(props) {
    /**
     * Renders a vertical progress bar to display things like Health and Energy.
     * Required props: {Name: str}, {MaxVal: int}, {CurrentVal: int}, {BgImage: .png}, {BgColour: "R,G,B"}, {Height: int}.
     * Optional props: {StatusFxBool: bool}, {StatusFx: icon.png}, {DepMax: int}
     * 
     * Name: Name of StatBar expressed as a string.
     * MaxVal: maximum value of stat expressed as an integer.
     * CurrentVal: current value of stat expressed as an integer.
     * BgImage: Background .png to outline StatBar, image size = (fill in later). 
     * BgColour: Colour of StatBar, should match name (health = red, energy = blue ,etc)
     * 
     * StatusFxBool: boolean for conditional render of a status effect field bellow StatBar.
     * StatusFx: icon.png of current status effect applied to StatBar.
     * DepMax: depreciated maximum value, expressed as an integer then converted to a percentage, greys out a portion of the top of the status bar.
     */
    
    const {Name, MaxVal, CurrentVal, BgImage, BgColour, Height, StatusFxBool, StatusFx, DepMax} = props

    const cValmValPer = ((CurrentVal / MaxVal) * 100)

    const containerStyles = {
        width: "1.5rem",
        height: Height,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        margin: 10
    }

    const MainBodyStyles = {
        height: "85%",
        width: "100%",
        backgroundColor: "#8c8c8c",
        borderRadius: "10px",
        position: "relative",
        display: "flex",
        justifyContent: "center",
        border: "2px solid black"

    }

    const BarStyles = {
        height: `${cValmValPer}%`,
        width: "100%",
        backgroundImage: `linear-gradient(rgba(${BgColour}, .4), rgba(${BgColour}, .9))`,
        borderRadius: "inherit",
        position: "absolute",
        bottom: 0,
        transition: 'height 1s ease-in-out'
    }

    const LabelStyles = {
        fontWeight: "bold",
    }

    return(
        <div className="StatBar" style={containerStyles}>
            <span style={LabelStyles}>{MaxVal}</span>
            <div style={MainBodyStyles}>
                <p style={{
                    writingMode:"vertical-rl",
                    fontWeight: "bold",  
                    textOrientation: "upright", 
                    letterSpacing: "-0.45rem", 
                    height: "100%",
                    zIndex: 1,
                    textAlign: "center"
                }}>{Name}</p>
                <div style={BarStyles}>
                </div>
            </div>
            <span style={LabelStyles}>{CurrentVal}</span>
        </div>
    )
}