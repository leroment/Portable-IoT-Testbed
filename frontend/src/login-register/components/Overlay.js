import React from "react";

const Overlay = (props) => {
  return (
    <div className="overlay-container">
      <div className="overlay">
        <div className="overlay-panel overlay-left">
          <h1>Already have an account?</h1>
          {/* <p className="overlay-description">
            If you already have an account,
            <br />
            login using your personal info.
          </p> */}
          <button
            className="ghost form-button"
            id="signIn"
            onClick={props.handleClickSignInButton}
          >
            Sign In
          </button>
        </div>
        <div className="overlay-panel overlay-right">
          <h1>Do not have an account?</h1>
          {/* <p className="overlay-description">
            Get Started,
            <br />
            Signup with your details.
          </p> */}
          <button
            className="ghost form-button"
            id="signUp"
            onClick={props.handleClickSignUpButton}
          >
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
};

export default Overlay;
