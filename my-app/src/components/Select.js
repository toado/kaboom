import React, { Component } from 'react'
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';



export default class Select extends Component {
    render() {

        return (
            <div className = "container-fluid">
                <div className = "row align-items-center justify-content-center">
                <DropdownButton variant = "success" id="dropdown-basic-button" title="Genre">
                    <Dropdown.Item href="#/action-1">Movie</Dropdown.Item>
                    <Dropdown.Item href="#/action-2">TV Show</Dropdown.Item>
                    <Dropdown.Item href="#/action-3">Anime</Dropdown.Item>
                </DropdownButton>
                </div>
            </div>
        )
    }
}
