import React from 'react'
import './Components/Home.css';
import './Components/ChatBot.css';

function ChatBot() {
    return (
        <div>
            <div className='chatbot_page'>
                Chat bot
            </div>
            <div className='chat_bot' style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '70h'}}>
                <iframe src="https://bot.dialogflow.com/0f48ba93-537d-4ce6-ac82-d518d9711afa"
                width = "700px"
                height = "550px">
                     
                </iframe>
            
            </div>
        </div>
    )
}

export default ChatBot
