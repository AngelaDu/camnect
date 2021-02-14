  import React from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import * as CgIcon from "react-icons/cg";
import './Log.css';
import { IconContext } from "react-icons";

const LoginButton = () => {
  const { loginWithRedirect, isAuthenticated } = useAuth0();

  return (
    !isAuthenticated && (
      <div className = 'login_box'>
        <button className = 'login' onClick={() => loginWithRedirect()}>
        <IconContext.Provider
          value={{ className: 'react-icons' }}>
              <CgIcon.CgLogIn />
        </IconContext.Provider>
          
          {'       Login'}
        </button>
      </div>

    )
  )
}

export default LoginButton;