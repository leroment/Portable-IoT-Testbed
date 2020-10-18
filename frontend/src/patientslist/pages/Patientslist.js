import React, {useEffect, useState } from 'react'
import { DataGrid } from "@material-ui/data-grid";
import axios from "axios";




function Patientslist() {

    const [patients, setPatients] = useState([])

    useEffect(() => {
        // axios.post(`/api/register`, {
        //     username: "andrewcai",
        //     email: "andrewcai19972011@gmail.com",
        //     password: "test123"
        // }).then((response) => {
        //     localStorage.setItem("token", response.data.token);
        // }).catch(err => {
        //     console.log(err);
        // });

        axios.get(`/api/patients`, {
            headers: { Authorization: `Token ${localStorage.getItem('token')}`}
        }).then((response) => {
            setPatients(response.data);
        })
    }, []);

    const columns = [
        { field: 'id', headerName: 'ID', width: 100 },
        { field: 'username', headerName: 'Username', width: 300 },
        { field: 'email', headerName: 'Email', width: 400 },
        { field: 'is_staff', headerName: 'Role', width: 100 },
    ]
    
    const rows = patients.map((p) => (
            {
                id: p.id,
                username: p.username,
                email: p.email,
                is_staff: p.is_staff
            }
        ))
      ;

    
    return (
        <div style={{ height: "40vh", width: "50vw" }}>
            <h1>Patients</h1>
            <p></p>
            <DataGrid rows={rows} columns={columns} pageSize={5} />
        </div>
    )
}

export default Patientslist
