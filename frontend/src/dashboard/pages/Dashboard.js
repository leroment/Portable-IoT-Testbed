import React, {useEffect, useState} from "react";
import axios from "axios";

const Dashboard = () => {
  const [accelerometer, setAccelerometer] = useState("");
  const [ecg, setEcg] = useState("");
  // const [eda, setEda] = useState("");
  // const [emg, setEmg] = useState("");


  useEffect(() => {
    axios.get(`/api/patients/${localStorage.getItem('id')}/patientdata`, {
      headers: {
        Authorization: `Token ${localStorage.getItem('token')}`
      }
    }).then((response) => {
      console.log(response.data);
      setAccelerometer(response.data[0].accelerometer[0].data_id ? response.data[0].accelerometer[0].data_id : "");
      setEcg(response.data[0].ecg[0].data_id ? response.data[0].ecg[0].data_id : "");
      // setEda(response.data[0].eda[0].data_id);
      // setEmg(response.data[0].emg[0].data_id);
    }).catch((err) => {
      console.log(err);
    });
  
  }, [])


  return (
    <div>
      <div>
        This is the dashboard page where you will see all the data from sensors
        <p>ECG: {ecg}</p>
        <p>Accelerometer: {accelerometer}</p>
      </div>
      <div>&nbsp;</div>
      {/* <iframe
        src="http://35.213.207.72/d-solo/NEBjJecGz/eda?orgId=1&panelId=2"
        width="900"
        height="400"
        frameborder="0"
        title="EDA Readings"
      ></iframe>{" "}
      &nbsp;
      <iframe
        src="http://35.213.207.72/d-solo/3smAf65Gk/ecg?orgId=1&panelId=2"
        width="900"
        height="400"
        frameborder="0"
        title="ECG Readings"
      ></iframe>
      <div>&nbsp;</div>
      <iframe
        src="http://35.213.207.72/d/QgrEB6cGk/glucose?orgId=1&viewPanel=2"
        width="900"
        height="400"
        frameborder="0"
        title="Glucose Readings"
      ></iframe>{" "}
      &nbsp;
      <iframe
        src="http://35.213.207.72/d-solo/08suBe5Gk/heart-rate?orgId=1&panelId=2"
        width="900"
        height="400"
        frameborder="0"
        title="Heart Rate"
      ></iframe> */}

        <iframe src={`http://35.213.207.72/d-solo/3smAf65Gk/ecg?orgId=1&refresh=5s&from=now-5m&to=now&var-token=${ecg}&theme=light&panelId=2`} width="900" height="400" frameborder="0"></iframe>
        &nbsp;
        <iframe src={`http://35.213.207.72/d-solo/08suBe5Gk/heart-rate?orgId=1&from=now-5m&to=now&var-token=${ecg}&refresh=5s&theme=light&panelId=2`} width="900" height="400" frameborder="0"></iframe>
        &nbsp;
        <iframe src={`http://35.213.207.72/d-solo/-2yAZWpGk/accelerometer?orgId=1&refresh=5s&var-token=${accelerometer}&from=now-5m&to=now&theme=light&panelId=2`} width="900" height="400" frameborder="0"></iframe>    
        </div>
  );
};

export default Dashboard;
