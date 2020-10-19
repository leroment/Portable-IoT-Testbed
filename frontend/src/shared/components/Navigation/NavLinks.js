import React, { useState } from "react";
import { NavLink, Redirect } from "react-router-dom";

import "./NavLinks.css";

// const isAuthenticated = () => {
//   console.log("from app js" + localStorage.getItem("token"));
//   return !!localStorage.getItem("token");
// };

const NavLinks = (props) => {
  const [redirectToLogin, setRedirectToLogin] = useState(false);

  if (redirectToLogin) {
    return <Redirect to="/" />;
  }

  const handleLogout = () => {
    localStorage.removeItem("token");
    setRedirectToLogin(true);
    //props.handleForceUpdate();
  };

  return (
    <ul className="nav-links">
      {props.authenticated && (
        <li>
          <NavLink to="/dashboard" exact>
            DASHBOARD
          </NavLink>
        </li>
      )}
      {props.authenticated && (
        <li>
          <NavLink to="/patientslist" exact>
            PATIENTS
          </NavLink>
        </li>
      )}
      {props.authenticated && (
        <li>
          <NavLink to="/alerts" exact>
            ALERTS
          </NavLink>
        </li>
      )}
      {!props.authenticated && (
        <li>
          <NavLink to="/" exact>
            LOGIN
          </NavLink>
        </li>
      )}
      {props.authenticated && (
        <li>
          <NavLink to="/" onClick={handleLogout} exact>
            SIGNOUT
          </NavLink>
        </li>
      )}
    </ul>
  );
};

export default NavLinks;
