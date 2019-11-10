import React, { Component } from 'react'
import '../App.css';


export default class Title extends Component {
    render() {
        
        return (
            <div className = "container-fluid">
                <div className = "row align-items-center justify-content-center">
                    <div className = "col-md-6">
                        <div className = 'title'>
                            Kaboom!
                        </div>
                        <div className = "description">
                            For all the indecisive movie watchers!
                        </div>
                    </div>
                </div>
            </div>

        )
    }
}
