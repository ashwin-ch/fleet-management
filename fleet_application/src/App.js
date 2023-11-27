import React,{useState, useEffect} from 'react'
import './App.css';
import { MenuProps, useStyles, equipments } from "./utils";
import ListEquipments from "./component/MultiselectDropdown";
import MaterialTable from '@material-table/core'
import equipmentsData from './component/data/equipments.json';


function App() {
  console.log("trying to connect localhost:4000/vehicles");
  // testing
  const socket = require("socket.io-client")("http://fleet-service:4000/vehicles");
  const socket_1 = require("socket.io-client")("http://0.0.0.0:4000/vehicles");
  const socket_2 = require("socket.io-client")("http://10.244.0.75:4000/vehicles");

  socket.on("connect_error", (err) => {
    console.log(`connect_error due to ${err.message}`);
  });
  socket_1.on("connect_error", (err) => {
    console.log(`connect_error due to ${err.message}`);
  });
  socket_2.on("connect_error", (err) => {
    console.log(`connect_error due to ${err.message}`);
  });
  const url = "http://10.244.0.75:4000/vehicles"
  const [data, setData] = useState([])
  useEffect(() => {
    getVehicles()
  }, [])

   //Fetch Equipment list from Equipments.json
  function getEquipments(data) {
    try {
      var equipmentsList  = data;
        if(typeof equipmentsList !== 'undefined'){
          equipmentsList =  equipmentsData.filter(item => equipmentsList.includes(item.id)).map(item => item.name).join(', ');
        }
      return equipmentsList;
    } catch (err) {
      console.log(err);
    }
  }


  //Fetch vehicle list from database
  async function getVehicles() {
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          accept: 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      const result = await response.json();
      return setData(result);
    } catch (err) {
      console.log(err);
    }
  }
  const columns = [
    { field: 'id', title: 'Vehicle ID', headerName: 'ID', width: 90 },
    {
      field: 'name',
      title: 'Vehicle Name',
      headerName: 'name',
      width: 150,
    },
    {
      title: 'Status',
      field: 'status',
      headerName: 'status',
      lookup: {active: "Active", inactive: "Inactive"},
      width: 150,
    },
    {
      title: 'Vehicle Name',
      field: 'fuelType',
      headerName: 'fuelType',
      lookup: {Diesel: "Diesel", CNG: "CNG", LNG: "LNG", Eletrical: "Eletrical"},
      width: 110,
    },
    {
      title: 'Equipments',
      field: 'equipments',
      headerName: 'equipments',
      sortable: false,
      width: 160,
      editComponent: (props) => {
        var equipmentsList = props.rowData.equipments;
        if(typeof equipmentsList !== 'undefined'){
          equipmentsList =  equipmentsData.filter(item => equipmentsList.includes(item.id)).map(item => item.name);
        }
        var dropDownmenu = <ListEquipments selectedEquipments={equipmentsList}/>;
        return (<ListEquipments selectedEquipments={equipmentsList ? equipmentsList : []}/>);
      },
      render: (rowData) =>
        {
          // var equipmentsList = rowData.equipments;
          // if(typeof equipmentsList !== 'undefined'){
          //   equipmentsList =  equipmentsData.filter(item => equipmentsList.includes(item.id)).map(item => item.name).join(', ');
          // }
          var equipmentsList = getEquipments(rowData.equipments)
          return equipmentsList;
        },
    }
  ]
  return (
    <div className="App">
     <MaterialTable
      title="Fleet Management Application"
      data={data}
      columns={columns}
      editable= {{
        onRowAdd: newRow => new Promise((resolve, reject) => {
          const updatedRow = [...data,{id:Math.floor(Math.random()*100),...newRow}]
          setTimeout(() => {
            setData(updatedRow)
          resolve()
          },2000)
        }),
        onRowDelete: (oldData) => new Promise((resolve, reject) => {
          //Backend call
          fetch(url + "/" + oldData.id, {
            method: "DELETE",
            headers: {
              'Content-type': "application/json"
            },

          }).then(resp => resp.json())
            .then(resp => {
              getVehicles()
              resolve()
            })
        }),
        onRowUpdate: (newData, oldData) => new Promise((resolve, reject) => {
          //Backend call
          fetch(url + "/" + oldData.id, {
            method: "PUT",
            headers: {
              'Content-type': "application/json"
            },
            body: JSON.stringify(newData)
          }).then(resp => resp.json())
            .then(resp => {
              getVehicles()
              resolve()
            })
        }),
      }}
      options={{
        actionsColumnIndex:-1, addRowPosition:'first'
      }}
     />
    </div>
  );
}

export default App;