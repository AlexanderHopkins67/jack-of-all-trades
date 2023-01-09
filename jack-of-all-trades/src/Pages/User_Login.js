import React, {useState} from "react";

export default function User_Login(props) {
    const [userInput, setUserInput] = useState()
    const [passInput, setPassInput] = useState()
    
        
    function handleSubmit(event) {
        event.preventDefault()
        props.login(userInput, passInput)
        console.log(userInput, passInput)
    }
    
    return(
        <div className="login">
            <h2>Jack of all Trades</h2>
            <h3>Login to play</h3>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input type={"text"} name="userInput" onChange={e => setUserInput(e.target.value)}/>
                    Password:
                    <input type={"text"} name="passInput" onChange={e => setPassInput(e.target.value)}/>
                </label>
                <input type={"submit"} value="submit"/>
            </form>
            <button onClick={handleSubmit}>test</button>
        </div>
    )
}