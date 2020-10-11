import React from "react";

const Dashboard = () => {
  return (
    <div>
      <div>
        This is the dashboard page where you will see all the data from sensors
      </div>
      <div>&nbsp;</div>
      <iframe
        src="http://localhost:3000/d-solo/c8J-K7dMz/andrews-ecg-readings?orgId=1&from=now-5m&to=now&refresh=5s&theme=light&panelId=4"
        width="900"
        height="400"
        frameborder="0"
        title="EDA Readings"
      ></iframe>{" "}
      &nbsp;
      <iframe
        src="http://localhost:3000/d-solo/c8J-K7dMz/andrews-ecg-readings?orgId=1&from=now-5m&to=now&refresh=5s&theme=light&panelId=2"
        width="900"
        height="400"
        frameborder="0"
        title="ECG Readings"
      ></iframe>
      <div>&nbsp;</div>
      <iframe
        src="http://localhost:3000/d-solo/c8J-K7dMz/andrews-ecg-readings?orgId=1&from=now-5m&to=now&refresh=5s&theme=light&panelId=6"
        width="900"
        height="400"
        frameborder="0"
        title="Glucose Readings"
      ></iframe>
    </div>
  );
};

export default Dashboard;
