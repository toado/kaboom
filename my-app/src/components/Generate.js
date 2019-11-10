import React, { Component } from 'react';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import Button from 'react-bootstrap/Button';

export default class Generate extends Component {

    constructor(props) {
        super(props)
    
        this.state = {
            movie: "",
            genre: ""
        }
    }

    async recommend() {
        let result = await fetch("https://56428d32.ngrok.io/", {
            method: "post",
            mode: "no-cors",
            headers: {
                'accept': 'application.json',
                'Content-type': 'application.json',
            },
            body: JSON.stringify({
                film: 'Dark Knight',
                genre: "Movie"
            })

        })
    }
    
    render() {
        return (
            <div className = "container-fluid">
                <div className = "row align-items-center justify-content-center">
                    <ButtonToolbar className = "generate">
                        <Button variant="success" onClick = {() => this.recommend()}>Recommend!</Button>
                    </ButtonToolbar>
                </div>
            </div>
        )
    }
}
