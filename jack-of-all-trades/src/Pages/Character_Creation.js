import React from "react"
import axios from "axios"

export default function Character_Creation () {
    function postNewCharacter() {
        const username = "alex"
        var formData = new FormData()
        formData.append("username", username)

        axios({
            method: "POST",
            url: "/api/newCharacter",
            data: formData
        })
    }
    return(
        <div>
            <h1>character creation</h1>
            <button onClick={postNewCharacter}>test</button>
        </div>
    )
}