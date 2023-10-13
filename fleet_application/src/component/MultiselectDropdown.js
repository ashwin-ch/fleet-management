import React from "react";
import {useState, useEffect} from 'react'
import { MenuProps, useStyles, equipments } from "../utils";
import Checkbox from "@material-ui/core/Checkbox";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import MenuItem from "@material-ui/core/MenuItem";
import Select from "@material-ui/core/Select";


function ListEquipments(selectedData){
  const [selected, setSelected] = useState(selectedData.selectedEquipments);
  const classes = useStyles();
  const isAllSelected =  equipments.length > 0 && selected.length === equipments.length;
    const handleChange = (event) => {
      const value = event.target.value;
      if (value[value.length - 1] === "all") {
        setSelected(selected.length === equipments.length ? [] : equipments);
        return;
      }
      setSelected(value);
    };
    return (
      <Select
        labelId="mutiple-select-label"
        multiple
        value={selected}
        onChange={handleChange}
        renderValue={(selected) => selected.join(", ")}
        MenuProps={MenuProps}
      >
        <MenuItem
          value="all"
          classes={{
            root: isAllSelected ? classes.selectedAll : ""
          }}
        >
          <ListItemIcon>
            <Checkbox
              classes={{ indeterminate: classes.indeterminateColor }}
              checked={isAllSelected}
              indeterminate={
                selected.length > 0 && selected.length < equipments.length
              }
            />
          </ListItemIcon>
          <ListItemText
            classes={{ primary: classes.selectAllText }}
            primary="Select All"
          />
        </MenuItem>
        {equipments.map((equipment) => (
          <MenuItem key={equipment} value={equipment}>
            <ListItemIcon>
              <Checkbox checked={selected.indexOf(equipment) > -1} />
            </ListItemIcon>
            <ListItemText primary={equipment} />
          </MenuItem>
          
        ))}
      </Select>
      
    );
}
export default ListEquipments;
