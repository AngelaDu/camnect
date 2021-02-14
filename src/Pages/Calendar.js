import React from 'react'
import { useAuth0 } from "@auth0/auth0-react";
import './Calendar.css';
import './Components/Home.css';


function Calendar() {

    const { user } = useAuth0();

    const str1 = "https://calendar.google.com/calendar/embed?src=";
    var email = "";

    if (user == undefined) {
        email = "";
    } else {
        email = user["email"];
    }

    const final_linked = str1.concat(email);

    return (
        <div >
            <div className='calendar_title'>
                Calendar
            </div>
        
        <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '70h'}}>
            
            <iframe src= { final_linked } 
            width = "800px"
            height = "600px" 
            ></iframe>
        </div>
        </div>
    )
}

export default Calendar
