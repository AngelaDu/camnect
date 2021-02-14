import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import './Log.css';
import { IconContext } from "react-icons";
import * as CgIcon from "react-icons/cg";

const LogoutButton = () => {
  const { logout, isAuthenticated } = useAuth0();

  return (
    isAuthenticated && (
        <div className = 'login_box'>
            <button className = 'login' onClick={() => logout()}>
             <IconContext.Provider
                  value={{ className: 'react-icons' }}>
                 <CgIcon.CgLogOut />
               </IconContext.Provider>
          
              {'       Logout'}
            </button>
        </div>
    )
  )
}

export default LogoutButton