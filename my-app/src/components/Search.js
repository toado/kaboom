import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import '../App.css';


export default class Search extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             filmName: ""
        }
    }

    filmNameChange = (event) => {
        console.log(event.target.value)
        this.setState({
            filmName: event.target.value 
        })

    }
    
    render() {
        return (
            <div className = "container-fluid">
                <div className = "row align-items-center justify-content-center">
                    <div>
                    <Form inline className = "searchBox input-large" value = {this.state.filmName} onChange = {this.filmNameChange}>
                        <FormControl type="text" placeholder="Search" />
                    </Form>
                    </div>
                </div>
            </div>

        )
    }
}
