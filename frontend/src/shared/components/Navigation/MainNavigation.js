import React, { useEffect, Component } from "react";
import { Link } from "react-router-dom";

import MainHeader from "./MainHeader";
import NavLinks from "./NavLinks";
import "./MainNavigation.css";

class MainNavigation extends Component {
  constructor(props) {
    super(props);
  }
  // handleForceUpdate() {
  //   this.forceUpdate();
 // }
  render() {
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
          <NavLinks
            authenticated={this.props.authenticated}
          />
        </nav>
      </MainHeader>
    );
  }
}

// const handleForceUpdate = () => {
//   this.forceUpdate();
// };

// const MainNavigation = (props) => {
//   return (
//     <MainHeader>
//       <button className="main-navigation__menu-btn">
//         <span />
//         <span />
//         <span />
//       </button>
//       <h1 className="main-navigation__title">
//         <Link to="/dashboard">Health Monitoring System</Link>
//       </h1>
//       <nav>
//         <NavLinks
//           authenticated={props.authenticated}
//           handleForceUpdate={handleForceUpdate}
//         />
//       </nav>
//     </MainHeader>
//   );
// };

export default MainNavigation;
