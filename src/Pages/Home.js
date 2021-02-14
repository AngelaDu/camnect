import React, { useState } from 'react'
import Profile from "./Components/Profile";
import './Components/Home.css';
import { Link, Route, Router, Switch } from 'react-router-dom';

import * as AiIcons from "react-icons/ai";
import * as BsIcons from "react-icons/bs";


function Home() {
    return (
        <div>
            <div className='home_page'>
                HOME
            </div>
            <div className='text_home'>
                Welcome to our web app! For our different features, please visit our different pages by opening the menu or pressing one of these buttons!
            </div>
            <li className='buttons'>
                <Link to = {'/calendar'} className = 'text_button'>
                     <AiIcons.AiFillHome />
                     {"  Calendar"}
                </Link>
            </li>
            <li className='buttons'>
                <Link to = {'/chatbot'} className = 'text_button'>
                     <BsIcons.BsFillChatDotsFill  />
                     {"  Chatbot"}
                </Link>
            </li>
        </div>
        
    )
}

export default Home
