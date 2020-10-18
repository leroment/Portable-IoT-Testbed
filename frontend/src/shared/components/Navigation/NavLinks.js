import React, {useState} from "react";
import { NavLink, Redirect } from "react-router-dom";

import "./NavLinks.css";

const NavLinks = ({ authenticated }) => {

  const [redirectToLogin, setRedirectToLogin] = useState(false);

  if (redirectToLogin) {
    return <Redirect to="/" />;
  }

  const handleLogout = () => {
    localStorage.removeItem("token");
    setRedirectToLogin(true);
  };

  return (
    <ul className="nav-links">
      <li>
        <NavLink to="/dashboard" exact>
          DASHBOARD
        </NavLink>
      </li>
      <li>
        <NavLink to="/patientslist" exact>
          PATIENTS
        </NavLink>
      </li>
      <li>
        <NavLink to="/alerts" exact>
          ALERTS
        </NavLink>
      </li>
      
      {!authenticated && (
          <li>
          <NavLink to="/" exact>
            LOGIN
          </NavLink>
        </li> )
      }
      {authenticated &&
          (
            <li>
            <NavLink to="/" >
              SIGNOUT
            </NavLink>
          </li>
          )
      }

    </ul>
  );
};

export default NavLinks;
