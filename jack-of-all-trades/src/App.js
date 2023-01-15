import './App.css';
import React, {useEffect, useState} from 'react';
import {Route, Routes, BrowserRouter} from "react-router-dom"
import Header from './Components/Header';
import Home from './Pages/Home';
import Error from './Pages/Error';
import GameDashboard from './Pages/GameDashboard';
import About from './Pages/About';
import User_Login from './Pages/User_Login';
import User_Dashboard from './Pages/User_Dashboard';
import Character_Creation from './Pages/Character_Creation';
import axios from "axios"

function App() {

  const [userCredential, setUserCredential] = useState(null)


  function loginHandle(username, password) {
    var formData = new FormData()
    formData.append("username", username)
    formData.append("password", password)

    axios({
      method: "POST",
      url: "/api/login",
      data: formData
    })
    .then((response) => {
      if (response.data !== null) {
        console.log(response.data)
        sessionStorage.setItem("sessionToken", response.data)
        setUserCredential(sessionStorage.getItem('sessionToken'))
      }
      })
    }

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={ <Header />}>
          <Route index element={<Home />}/>
          <Route path='about' element={<About />}/>
          <Route path='*' element={<Error />} />
        </Route>
        <Route path='/joat-dashboard' element={<GameDashboard />}>
          <Route index element={userCredential ? <User_Dashboard/> : <User_Login login={loginHandle}/>}/>
          <Route path='/joat-dashboard/character-creation' element={<Character_Creation />} />

        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App;
