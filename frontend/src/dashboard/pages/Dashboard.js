import React from "react";

const Dashboard = () => {
  return (
    <div>
      <div>
        This is the dashboard page where you will see all the data from sensors
      </div>
      <div>&nbsp;</div>
      <iframe
        src="http://35.213.207.72/d-solo/NEBjJecGz/eda?orgId=1&from=1602386665250&to=1602388760640&panelId=2"
        width="900"
        height="400"
        frameborder="0"
        title="EDA Readings"
      ></iframe>{" "}
      &nbsp;
      <iframe
        src="http://35.213.207.72/d-solo/3smAf65Gk/ecg?orgId=1&from=1602821914787&to=1602823201148&panelId=2"
        width="900"
        height="400"
        frameborder="0"
        title="ECG Readings"
      ></iframe>
      <div>&nbsp;</div>
      <iframe
        src="http://35.213.207.72/d/QgrEB6cGk/glucose?orgId=1&from=1602393057927&to=1602393374181&viewPanel=2"
        width="900"
        height="400"
        frameborder="0"
        title="Glucose Readings"
      ></iframe>{" "}
      &nbsp;
      <iframe
        src="http://35.213.207.72/d-solo/08suBe5Gk/heart-rate?orgId=1&from=1595219928303&to=1602992328303&panelId=2"
        width="900"
        height="400"
        frameborder="0"
        title="Heart Rate"
      ></iframe>
    </div>
  );
};

export default Dashboard;
