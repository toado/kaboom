import React, { Component } from 'react'
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';



export default class Select extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
            genreName: "Movie"     
        }
    }

    genreSelected(_, event) {
        console.log(event.target.title)
        this.setState({
            genreName: event.target.title
        })
    }

    
    render() {

        return (
            <div className = "container-fluid">
                <div className = "row align-items-center justify-content-center">
                <DropdownButton title = {this.state.genreName} onSelect = {this.genreSelected.bind(this)} variant="success" id="dropdown-basic-button">
                    <Dropdown.Item title = "Movie">Movie</Dropdown.Item>
                    <Dropdown.Item title = "TV Show">TV Show</Dropdown.Item>
                    <Dropdown.Item title = "Anime">Anime</Dropdown.Item>
                </DropdownButton>
                </div>
            </div>
        )
    }
}
