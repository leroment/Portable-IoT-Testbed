import React, {useEffect, useState } from 'react'
import { DataGrid } from "@material-ui/data-grid";
import axios from "axios";


const columns = [
    { field: 'id', headerName: 'ID', width: 100 },
    { field: 'username', headerName: 'Username', width: 300 },
    { field: 'email', headerName: 'Email', width: 400 },
    { field: 'is_staff', headerName: 'Role', width: 100 },
]

const rows = [
    { id: 1, username: 'Snow', email: 'Jon', is_staff: 35 },
    { id: 2, username: 'Lannister', email: 'Cersei', is_staff: 42 },
    { id: 3, username: 'Lannister', email: 'Jaime', is_staff: 45 },
    { id: 4, username: 'Stark', email: 'Arya', is_staff: 16 },
    { id: 5, username: 'Targaryen', email: 'Daenerys', is_staff: null },
    { id: 6, username: 'Melisandre', email: null, is_staff: 150 },
    { id: 7, username: 'Clifford', email: 'Ferrara', is_staff: 44 },
    { id: 8, username: 'Frances', email: 'Rossini', is_staff: 36 },
    { id: 9, username: 'Roxie', email: 'Harvey', is_staff: 65 },
  ];

function Patientslist() {

    useEffect(() => {
        axios.post(`/api/login`, {
            username: "andrewcai",
            password: "test123"
        }).then((response) => {
            localStorage.setItem("token", response.data.token);
        }).catch(err => {
            console.log(err);
        });
    }, []);



    
    return (
        <div style={{ height: "40vh", width: "50vw" }}>
            <h1>Patients</h1>
            <p></p>
            <DataGrid rows={rows} columns={columns} pageSize={5} />
        </div>
    )
}

export default Patientslist
