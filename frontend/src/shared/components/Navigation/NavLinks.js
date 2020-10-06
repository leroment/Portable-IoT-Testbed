import React from "react";
import { NavLink } from "react-router-dom";

import "./NavLinks.css";

const NavLinks = (props) => {
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
      <li>
        <NavLink to="/" exact>
          LOGIN
        </NavLink>
      </li>
      <li>
        <NavLink to="/" exact>
          SIGNOUT
        </NavLink>
      </li>
    </ul>
  );
};

export default NavLinks;
