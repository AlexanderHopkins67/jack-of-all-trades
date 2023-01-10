import React from "react";

export default function StatBar(props) {
    /**
     * Renders a vertical progress bar to display things like Health and Energy.
     * Required props: {MaxVal: int}, {CurrentVal: int}, {BgImage: .png}.
     * Optional props: {StatusFxBool: bool}, {StatusFx: icon.png}, {DepMax: int}
     * 
     * MaxVal: maximum value of stat expressed as an integer.
     * CurrentVal: current value of stat expressed as an integer.
     * BgImage: Background .png to outline StatBar, image size = (fill in later). 
     * 
     * StatusFxBool: boolean for conditional render of a status effect field bellow StatBar.
     * StatusFx: icon.png of current status effect applied to StatBar.
     * DepMax: depreciated maximum value, expressed as an integer then converted to a percentage, greys out a portion of the top of the status bar.
     */
    return(
        <div>
            
        </div>
    )
}