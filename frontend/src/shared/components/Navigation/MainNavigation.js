import React from "react";
import { Link } from "react-router-dom";

import MainHeader from "./MainHeader";
import NavLinks from "./NavLinks";
import "./MainNavigation.css";

const MainNavigation = ({authenticated}) => {
  return (
    <MainHeader>
      <button className="main-navigation__menu-btn">
        <span />
        <span />
        <span />
      </button>
      <h1 className="main-navigation__title">
        <Link to="/dashboard">Health Monitoring System</Link>
      </h1>
      <nav>
        <NavLinks authenticated={authenticated} />
      </nav>
    </MainHeader>
  );
};

export default MainNavigation;
