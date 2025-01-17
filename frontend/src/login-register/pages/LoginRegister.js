import React, { useState } from "react";

import "../main.css";
import Login from "../components/Login";
import SignUp from "../components/SignUp";
import Overlay from "../components/Overlay";

const LoginRegister = () => {
  const [rightPanelActive, setRightPanelActive] = useState(false);

  return (
    <div className="main" style={{display: "flex", justifyContent: "center", alignItems: "center", height: "100%", width: "100%"}}>
      <div
        className={`container ${rightPanelActive ? `right-panel-active` : ``}`}
      >
        <SignUp />
        <Login />
        <Overlay
          handleClickSignInButton={() => {
            console.log("clicked singin button");
            setRightPanelActive(false);
          }}
          handleClickSignUpButton={() => {
            setRightPanelActive(true);
          }}
        />
      </div>
    </div>
  );
};

export default LoginRegister;
